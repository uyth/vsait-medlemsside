$(document).ready(() => {
	console.log('detail.js loaded');
	// registration form
	const submit = $("button.btn").get(0);
	$(submit).on('click', function(e){
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
			cancelButtonText: "Avbryt",
			confirmButtonText: alertInfo.confirmButtonText,
		}).then((result) => {
			if (result.isConfirmed) {
				// Add event_id
				form.append(`<input type="hidden" name="event_id" value="${this.value}"/>`);
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
	})
	// Show users
	const showBtn = $(".show_people").get(0);
	console.log(showBtn)
	$(showBtn).on('click', function(e){
		e.preventDefault();
		Swal.fire({
			title: "Liste over påmeldte",
			html: $(".display_users").get(0).innerHTML,
			showCancelButton: true,
			showConfirmButton: false,
			cancelButtonColor: '#d33',
			cancelButtonText: "Lukk.",
		})
	});
});

const getInfo = function(id) {
	console.log(id)
	const info = {}
	if (id === "register") {
		info.title = "Bekreftelse!";
		info.text = "Du melder deg nå på arrangementet";
		info.icon = 'warning';
		info.confirmButtonText = 'Ok, meld meg på';
		// success
		info.s_title = 'Registrert!';
		info.s_text = 'Du er nå meldt på arrangementet';
	} else if (id === "cancel_registration") {
		info.title = "Advarsel!";
		info.text = "Du blir nå meldt av arrangementet";
		info.icon = 'warning';
		info.confirmButtonText = "Ok, meld meg av";
		// success
		info.s_title = 'Avregistrert!';
		info.s_text = 'Du er nå meldt ut av arrangementet';
	} else if (id === "cancel_waiting") {
		info.title = "Advarsel!";
		info.text = "Du er i ferd med å melde deg av ventelisten. Du vil miste plassen din i køen";
		info.icon = 'warning';
		info.confirmButtonText = 'Ok, meld meg av';
		// success
		info.s_title = 'Avregistrert venteliste!';
		info.s_text = 'Du er ikke lenger på ventelisten i arrangementet';
	}
	return info
}
