$(document).ready(() => {
  console.log("events.js loaded");
  // HELPTEXT for PEOPLE
  const people_div = $(".field-max_people").children().get(0);
  people_div.innerHTML +=
    "<div class='help'>Setting max people to 0 or less than 0 means unlimited people</div>";

  // Fix tinyMCE input width size
  setTimeout(() => ($(".tox.tox-tinymce").get(0).style.width = "100%"), 1500);

  // påmeldingsfrist <= avmeldingsfrist <= starttid < sluttid
  const submit_row = $(".submit-row").get(0);
  const submit_row_children = $(".submit-row").children();
  const save_another = submit_row_children[2];
  const save_continue = submit_row_children[3];
  const save_end = submit_row_children[0];
  const saves = [save_another, save_continue, save_end];
  for (save of saves) {
    // Hide save button
    save.style.display = "none";
    // Make a clone
    const input = document.createElement("a");
    input.innerText = save.value;
    input.className = "button";
    input.style.padding = "10px 15px";
    input.style.position = "relative";
    input.style.top = "9px";
    input.style.margin = "5px";
    $(input).click(function () {
      const startTime_date = $("#id_startTime_0").get(0);
      const startTime_time = $("#id_startTime_1").get(0);
      const endTime_date = $("#id_endTime_0").get(0);
      const endTime_time = $("#id_endTime_1").get(0);
      const registrationDeadline_date = $("#id_registrationDeadline_0").get(0);
      const registrationDeadline_time = $("#id_registrationDeadline_1").get(0);
      const cancellationDeadline_date = $("#id_cancellationDeadline_0").get(0);
      const cancellationDeadline_time = $("#id_cancellationDeadline_1").get(0);
      const startTime = new Date(
        startTime_date.value + " " + startTime_time.value
      );
      const endTime = new Date(endTime_date.value + " " + endTime_time.value);
      const registrationDeadline = new Date(
        registrationDeadline_date.value + " " + registrationDeadline_time.value
      );
      const cancellationDeadline = new Date(
        cancellationDeadline_date.value + " " + cancellationDeadline_time.value
      );
      // If timedate is valid, check for time validity given: påmeldingsfrist <= avmeldingsfrist <= starttid < sluttid
      // else proceed as normal
      if (
        isValid(startTime) &&
        isValid(endTime) &&
        isValid(registrationDeadline) &&
        isValid(cancellationDeadline)
      ) {
        console.log("All valid");
        if (
          registrationDeadline <= cancellationDeadline &&
          cancellationDeadline <= startTime &&
          startTime < endTime
        ) {
          console.log("Saving..");
          save.click();
        } else {
          console.log("Error..");
          Swal.fire({
            title: "Time validation error!",
            html: "Make sure to set valid times!<br/></br>påmeldingsfrist <= avmeldingsfrist <= starttid < sluttid",
            icon: "error",
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: "Okay",
            timer: 5000,
          });
        }
      } else {
        save.click();
      }
    });
    submit_row.appendChild(input);
  }
});

const isValid = function (time) {
  return !isNaN(time.getTime());
};
