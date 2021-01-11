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

	// Success
	const success = $("p.success").get(0);
	if (success) {
		Swal.fire({
			title: "Success!",
			text: "We've registered your attendance!",
			icon: "success",
			showConfirmButton: true,
			timer: 1500,
			confirmButtonColor: '#3085d6',
			confirmButtonText: "Ok."
		})
	}
	// Error
	const error = $("p.error").get(0);
	if (error) {
		Swal.fire({
			title: "Error!",
			html: "Your attendance didn't register! <br/><br/>"+error.innerText,
			icon: "error",
			showConfirmButton: true,
			timer: 1500,
			confirmButtonColor: '#3085d6',
			confirmButtonText: "Ok."
		})
	}
});
