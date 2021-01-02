$(document).ready(() => {
	console.log('datetime_field.js loaded');

	const startTime_time = $("#id_startTime_1");
	const endTime_time = $("#id_endTime_1");
	// Add event for inputs
	startTime_time.keyup(() => serialize(startTime_time));
	startTime_time.change(() => serialize(startTime_time));
	endTime_time.keyup(() => serialize(endTime_time));
	endTime_time.change(() => serialize(endTime_time));

	// Init serializer
	serialize(startTime_time);
	serialize(endTime_time);

	// Add events for "now" and "time chooser"
	setTimeout(() => {
		const clockbox0 = $("#clockbox0");
		const clockbox0_children = [...clockbox0.get(0).children[1].children, clockbox0.get(0).children[2], $("#id_startTime_1 + .datetimeshortcuts").get(0).children[0]];
		for (const child of clockbox0_children) {
			child.addEventListener("click", () => serialize(startTime_time));
		}
		const clockbox1 = $("#clockbox1");
		const clockbox1_children = [...clockbox1.get(0).children[1].children, clockbox1.get(0).children[2], $("#id_endTime_1 + .datetimeshortcuts").get(0).children[0]];
		for (const child of clockbox1_children) {
			child.addEventListener("click", () => serialize(endTime_time));
		}
	},1000);
});

const serialize = function(obj) {
	obj = obj.get(0);
	let tokens = obj.value.split(":").slice(0,2);
	tokens[0] = tokens[0].substring(0,2);
	tokens[1] = tokens[1].substring(0,2);
	obj.value = tokens[0]+":"+tokens[1];
}
