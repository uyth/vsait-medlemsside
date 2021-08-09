$(document).ready(() => {
	console.log('forgot_password.js loaded');
	const submit = $("#email").get(0);
	if (submit) {
		const form = $($(submit).parents('form').get(0));
		$(form).on('submit', function(e) {
			e.preventDefault();
			console.log(submit.value)
			$.ajax({
				type: 'POST',
				url: window.location.href,
				data: $(form).serialize(),
				success: function() {
					Swal.fire({
						title: "E-post har blitt sendt!",
						html: "En melding har blitt sent til din e-post om det finnes en bruker som er registrert med eposten oppgitt.<br/>I meldingen vil du få en lenke som sender deg videre til et skjema hvor du får mulighet til å endre passordet ditt.",
						icon: "warning",
						showCancelButton: false,
						confirmButtonColor: '#3085d6',
						cancelButtonColor: '#d33',
						confirmButtonText: "Ok",
					}).then(function() {
						submit.value = "";
					})
				},
				error: function() {
					Swal.fire({
						title: "Couldn't be sent!",
						html: "An error happened...",
						icon: "error",
						showCancelButton: false,
						confirmButtonColor: '#3085d6',
						cancelButtonColor: '#d33',
						confirmButtonText: "Ok",
					});
				}
			});
		});
	}
});

