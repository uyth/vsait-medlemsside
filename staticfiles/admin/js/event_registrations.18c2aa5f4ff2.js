$(document).ready(() => {
  console.log("event_registrations.js loaded");

  const id_registrations = $("#id_registrations");
  const id_registrations_children = $("#id_registrations").children().get();
  const div_registrations_parent = $("#id_registrations").parent().get(0);

  const id_waiting_list = $("#id_waiting_list");
  const id_waiting_list_children = $("#id_waiting_list").children().get();
  const div_waiting_list_parent = $("#id_waiting_list").parent().get(0);

  // Default states
  id_registrations.hide();
  id_waiting_list.hide();
  // Helptext
  div_registrations_parent.innerHTML +=
    "<div class='help' style='margin: 0 0 5px 0'>Select/deselect registrations by clicking on the users respectively</div>";
  div_waiting_list_parent.innerHTML +=
    "<div class='help' style='margin: 0 0 5px 0'>Select/deselect waiting_list by clicking on the users respectively</div>";
  div_registrations_parent.classList.add("0");
  div_waiting_list_parent.classList.add("1");
  // Table values
  const names = [];
  const registered_names = [];
  const waiting_list_names = [];
  const nameTypes = [registered_names, waiting_list_names];
  const header = ["firstname", "lastname", "email"];
  // Populates registered users and their checkboxes respectively
  for (let i = 0; i < id_registrations_children.length; i++) {
    const el = id_registrations_children[i];
    if (el.children[0].children[0].checked) {
      registered_names.push(el.children[0].innerText.trim() + " ; " + i);
    }
    names.push(el.children[0].innerText.trim() + " ; " + i);
  }
  for (let i = 0; i < id_waiting_list_children.length; i++) {
    const el = id_waiting_list_children[i];
    if (el.children[0].children[0].checked) {
      waiting_list_names.push(el.children[0].innerText.trim() + " ; " + i);
    }
  }
  // Create "Add users link"
  let add_user_anchor = document.createElement("a");
  add_user_anchor.href = "javascript:void(0)";
  add_user_anchor.innerText = "Add users";
  add_user_anchor.className = "addlink registration_anchor";
  div_registrations_parent.appendChild(add_user_anchor);
  add_user_anchor = document.createElement("a");
  add_user_anchor.href = "javascript:void(0)";
  add_user_anchor.innerText = "Add users";
  add_user_anchor.className = "addlink waiting_list_anchor";
  div_waiting_list_parent.appendChild(add_user_anchor);

  // Function to create table with corresponding names and headers
  const createTable = (
    name_array,
    header,
    div_parent,
    div_location,
    hidden
  ) => {
    // Creating tablewrapper
    const tableWrapper = document.createElement("div");
    tableWrapper.className = "tableWrapper";
    // Creating table
    const table = document.createElement("table");
    table.className = "event_registrations_table";
    // Create header
    const header_row = document.createElement("tr");
    for (th_text of header) {
      const th = document.createElement("th");
      th.innerText = th_text;
      header_row.appendChild(th);
    }
    header_row.className = "header_row";
    table.appendChild(header_row);
    // Create name elements
    for (elements_string of name_array) {
      const tr = document.createElement("tr");
      const elements = elements_string.split(" ; ");
      // console.log(elements)
      for (let j = 0; j < elements.length - 1; j++) {
        const td = document.createElement("td");
        td.innerText = elements[j];
        tr.appendChild(td);
      }
      // Get default color
      const i = +elements[elements.length - 1];
      const label = div_parent.children[1].children[i].children[0];
      const checkbox = label.children[0];
      if (checkbox.checked) {
        tr.classList.add("toggleOn");
      } else {
        tr.classList.remove("toggleOn");
      }
      // Onclick event
      tr.value = i;
      $(tr).click(function () {
        const label = div_parent.children[1].children[this.value].children[0];
        label.click();
        // Change color
        const checkbox = label.children[0];
        const nameArr = nameTypes[+div_parent.classList[0]];
        if (checkbox.checked) {
          this.classList.add("toggleOn");
          nameArr.push(name_array[this.value]);
        } else {
          this.classList.remove("toggleOn");
          for (let j = 0; j < nameArr.length; j++) {
            if (name_array[this.value] === nameArr[j]) {
              nameArr.splice(j, 1);
              break;
            }
          }
        }
        // console.log(name_array[this.value],div_parent.classList[0])
      });
      table.appendChild(tr);
    }
    if (hidden) {
      table.style.display = "none";
      tableWrapper.classList.add("popup_table");
    }
    tableWrapper.appendChild(table);
    div_location.appendChild(tableWrapper);
    div_location.classList.add("event_registrations_table");
  };
  const removeTables = function (div_parent) {
    while (div_parent.children.length > 4) {
      div_parent.lastChild.remove();
    }
  };
  const createTables = function () {
    removeTables(div_registrations_parent);
    removeTables(div_waiting_list_parent);
    createTable(
      registered_names,
      header,
      div_registrations_parent,
      div_registrations_parent,
      false
    );
    createTable(
      names,
      header,
      div_registrations_parent,
      div_registrations_parent,
      true
    );
    createTable(
      waiting_list_names,
      header,
      div_waiting_list_parent,
      div_waiting_list_parent,
      false
    );
    createTable(
      names,
      header,
      div_waiting_list_parent,
      div_waiting_list_parent,
      true
    );
  };
  createTables();

  const makePopup = function (table_id) {
    // Make table visible
    $(".popup_table").children().get(table_id).style.display = "table";
    // Alert/popup table
    Swal.fire({
      title: "Add users",
      html: $(".popup_table").get(table_id),
      showCancelButton: false,
      confirmButtonColor: "#3085d6",
      confirmButtonText: "Done",
    }).then(() => {
      console.log("a");
      createTables();
    });
  };
  // Display table
  $(".registration_anchor").on("click", () => makePopup(0));
  $(".waiting_list_anchor").on("click", () => makePopup(1));

  // Checkin-url
  const secret_url = $(id_secret_url).get(0).value;
  const event_id = +window.location.pathname
    .split("/")
    .filter((x) => x.length > 0 && x.length <= 4)[0];
  $(".field-secret_url").get(
    0
  ).innerHTML += `<div><a href='/events/${event_id}/${secret_url}' target='_blank' >Open checkin form</div>`;
});
