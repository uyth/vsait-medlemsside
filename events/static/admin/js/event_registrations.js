$(document).ready(() => {
	console.log('event_registrations.js loaded');

	const id_registrations = $("#id_registrations");
	const id_registrations_children = $("#id_registrations").children().get();
	const div_registrations_parent = $("#id_registrations").parent().get(0);

	const id_waiting_list = $("#id_waiting_list");
	const div_waiting_list_parent = $("#id_waiting_list").parent().get(0);

	// Default states
	id_registrations.hide();
	id_waiting_list.hide();
	// Helptext
	div_registrations_parent.innerHTML += "<div class='help' style='margin: 0 0 5px 0'>Select/deselect registrations by clicking on the users respectively</div>";
	div_waiting_list_parent.innerHTML += "<div class='help' style='margin: 0 0 5px 0'>Select/deselect waiting_list by clicking on the users respectively</div>";
	// HELPTEXT for PEOPLE
	const people_div = $(".field-max_people").children().get(0);
	people_div.innerHTML += "<div class='help'>Setting max people to 0 means unlimited people</div>"

	// Table values
	const name = [];
	const header = ["firstname","lastname","email"];
	// Register users name and their checkboxes respectively
	for (el of id_registrations_children) {
		name.push(el.children[0].innerText.trim());
	}
	// Function to create table with corresponding names and headers
	const createTable = (name,header,div_parent) => {
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
		table.appendChild(header_row)
		// Create name elements
		let i = 0;
		for (elements_string of name) {
			const tr = document.createElement("tr");
			const elements = elements_string.split(" ; ");
			console.log(elements)
			for (text of elements) {
				const td = document.createElement("td");
				td.innerText = text;
				tr.appendChild(td);
			}
			// Get default color
			const label = div_parent.children[1].children[i].children[0];
			const checkbox = label.children[0];
			if (checkbox.checked) {
				tr.classList.add("toggleOn");
			} else {
				tr.classList.remove("toggleOn");
			}
			// Onclick event
			tr.value = i;
			$(tr).click(function() {
				const label = div_parent.children[1].children[this.value].children[0];
				label.click()
				// Change color
				const checkbox = label.children[0];
				if (checkbox.checked) {
					this.classList.add("toggleOn");
				} else {
					this.classList.remove("toggleOn");
				}
			});
			table.appendChild(tr)
			i++;
		}
		div_parent.appendChild(table);
		div_parent.classList.add("event_registrations_table");
	}
	createTable(name, header, div_registrations_parent);
	createTable(name, header, div_waiting_list_parent);
});

