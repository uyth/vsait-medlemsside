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
			title: "Registered users",
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
		info.title = "Are you sure?";
		info.text = "You will be registering to this event!";
		info.icon = 'warning';
		info.confirmButtonText = 'Yes, register me!';
		// success
		info.s_title = 'Registered!';
		info.s_text = 'You have been successfully registered to this event!';
	} else if (id === "cancel_registration") {
		info.title = "Are you sure?";
		info.text = "You will be cancelling your registration to this event!";
		info.icon = 'warning';
		info.confirmButtonText = 'Yes, cancel the registration!';
		// success
		info.s_title = 'Cancelled registration!';
		info.s_text = 'You have successfully cancelled your registration to this event!';
	} else if (id === "cancel_waiting") {
		info.title = "Are you sure?";
		info.text = "You will be cancelling your waiting_list position to this event!";
		info.icon = 'warning';
		info.confirmButtonText = 'Yes, cancel your registration!';
		// success
		info.s_title = 'Cancelled waiting list registration!';
		info.s_text = 'You have successfully cancelled your waiting_list registration to this event!';
	}
	return info
}
