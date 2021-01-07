$(document).ready(() => {
	console.log('profile.js loaded');
	// registration form
	const foodBtn = $("#food").get(0);
	const passwordBtn = $("#password").get(0);
	const membershipBtn= $("#membership").get(0);
	if ($("#alert").get(0)) {
		// Alert message after password change found
		const alert = $("#alert").get(0);
		$(alert).hide();
		const alertInfo = {};
		if (alert.className === "success") {
			alertInfo.title = "Success!";
			alertInfo.text = "Du har endret ditt passord!";
			alertInfo.icon = "success";
		} else {
			alertInfo.title = "Error!";
			alertInfo.text = "Se og fiks erroren nedenfor!";
			alertInfo.icon = "error";
		}
		Swal.fire({
			title: alertInfo.title,
			text: alertInfo.text,
			icon: alertInfo.icon,
			timer: 1500,
			showCancelButton: false,
			showConfirmButton: false,
		})
	}
	$(foodBtn).on('click', click);
	$(passwordBtn).on('click', click2);
	$(membershipBtn).on('click', click3);
});

const click = function(e) {
	e.preventDefault();
	const form = $($(this).parents('form').get(0));
	console.log(form)
	const alertInfo = getInfo(this.id);
	Swal.fire({
		title: alertInfo.title,
		text: alertInfo.text,
		icon: alertInfo.icon,
		showCancelButton: true,
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: alertInfo.confirmButtonText,
	}).then((result) => {
		if (result.isConfirmed) {
			Swal.fire({
				title: alertInfo.s_title,
				text: alertInfo.s_text,
				icon: 'success',
				timer: 1500,
				showCancelButton: false,
				showConfirmButton: false,
			}).then(function() {
				form.submit();
			})
		}
	})
}
const click2 = function(e) {
	e.preventDefault();
	const form = $($(this).parents('form').get(0));
	const alertInfo = getInfo(this.id);
	Swal.fire({
		title: alertInfo.title,
		text: alertInfo.text,
		icon: alertInfo.icon,
		showCancelButton: true,
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: alertInfo.confirmButtonText,
	}).then((result) => {
		if (result.isConfirmed) {
			form.submit();
		}
	})
}
const click3 = function(e) {
	e.preventDefault();
	const form = $($(this).parents('form').get(0));
	const alertInfo = getInfo(this.id);
	Swal.fire({
		title: "BLI MEDLEM",
		html: "Som medlem kan du bli med på arrangementer.<br/><br/>Merk at du også må betale x nok til<br/><br/>1234 12 1234",
		icon: alertInfo.icon,
		showCancelButton: true,
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: "OK.",
		input: 'checkbox',
		inputPlaceholder: 'Jeg har lest.'
	}).then(function(result) {
		if (result.value) {
			Swal.fire({
				icon: 'success',
				text: 'SUCCESS MESSAGE MEMBERSHIP ADD!',
				timer: 1500,
				showCancelButton: false,
				showConfirmButton: false,
			}).then(function() {
				form.submit();
			})
		} else if (result.value === 0) {
			Swal.fire({
				icon: 'error',
				text: "Please make sure to read the text and check the box :(",
				timer: 1500,
				showCancelButton: false,
				showConfirmButton: false,
			});
		} else {
			console.log(`modal was dismissed by ${result.dismiss}`)
		}
	})
}
const getInfo = function(id) {
	console.log(id)
	const info = {}
	if (id === "food") {
		info.title = "Are you sure?";
		info.text = "Du endrer nå ditt matbehov.";
		info.icon = 'warning';
		info.confirmButtonText = 'Yes!';
		// success
		info.s_title = 'Endret!';
		info.s_text = 'Du har endret ditt matbehov!';
	} else if (id === "password") {
		info.title = "Are you sure?";
		info.text = "Du endrer nå ditt passord.";
		info.icon = 'warning';
		info.confirmButtonText = 'Yes!';
	}
	return info
}
