$(document).ready(() => {
	console.log('detail.js loaded');
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
