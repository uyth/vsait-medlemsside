$(document).ready(() => {
	console.log('events.js loaded');
	// HELPTEXT for PEOPLE
	const people_div = $(".field-max_people").children().get(0);
	people_div.innerHTML += "<div class='help'>Setting max people to 0 or less than 0 means unlimited people</div>"
});

