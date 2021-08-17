$(document).ready(() => {
	console.log('detail.js loaded');
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
			cancelButtonText: "Lukk",
		})
	});

	// Success
	const success = $("p.success").get(0);
	if (success) {
		Swal.fire({
			title: "Vellykket!",
			text: "Vi har registret ditt oppmøte!",
			icon: "success",
			showConfirmButton: false,
			timer: 2000,
		})
	}
	// Error
	const error = $("p.error").get(0);
	if (error) {
		Swal.fire({
			title: "Feilmelding!",
			html: "Oppmøtet ble ikke regisrert! <br/><br/>"+error.innerText,
			icon: "error",
			showConfirmButton: true,
			confirmButtonColor: '#3085d6',
			confirmButtonText: "Ok"
		})
	}
});
