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
						title: "Email har blitt sendt!",
						html: "En melding har blitt sent til ditt email om det finnes en bruker registrert med emailet.<br/>I mailet vil du få en lenke som sender deg videre til en skjema hvor du får endret passordet ditt.",
						icon: "warning",
						showCancelButton: false,
						confirmButtonColor: '#3085d6',
						cancelButtonColor: '#d33',
						confirmButtonText: "OK.",
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
						confirmButtonText: "OK.",
					});
				}
			});
		});
	}
});

