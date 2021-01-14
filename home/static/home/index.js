$(document).ready(() => {
	console.log('index.js loaded');
	membership_alert();
	confirmEmail_alert();
	no_account_alert();
	// Show password
	const show_password = $(".show_password a");
	show_password.on('click',function() {
		const input_password = $(this).parent().siblings().get(0);
		input_password.type = (input_password.type === "password") ? "text" : "password";
		show_password.get(0).innerText = (input_password.type === "password") ? "Vis" : "Skjul";
	});
});

const no_account_alert = function() {
	const alert = $("p.error").get(0);
	if (alert) {
		Swal.fire({
			title: "Bruker ikke funnet!",
			html: "Emailen du har oppgitt, tilhører ikke noen konto. Kontrollerer emailen og prøv på nytt.",
			icon: "error",
			showCancelButton: false,
			confirmButtonColor: '#3085d6',
			confirmButtonText: "OK.",
		});
	}
}

const confirmEmail_alert = function() {
	const alert = $("p.warning").get(0);
	if (alert) {
		Swal.fire({
			title: "Du må aktivere brukeren først!",
			html: "Du har tidligere fått sent mail om å aktivere brukeren.<br/>Har ikke fått noe mail?<br/><a href='javascript:void(0)'>Trykk her for å sende på nytt.</a>",
			icon: "error",
			showCancelButton: false,
			confirmButtonColor: '#3085d6',
			confirmButtonText: "OK.",
		});
	}
}

const membership_alert = function() {
	const alert = $("#alert_not_read").get(0);
	if (alert) {
		const form = $($(alert).parents('form').get(0));
		setTimeout(() => {
			Swal.fire({
				title: "Husk å bli medlem!",
				html: "Som medlem kan du bli med på arrangementer<br/>Bli medlem ved å gå inn på din profil!",
				icon: "warning",
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
						text: 'This message will no longer show up.',
						timer: 1500,
						showCancelButton: false,
						showConfirmButton: false,
					}).then(function() {
						form.submit();
					})
				} else if (result.value === 0) {
					Swal.fire({
						icon: 'error',
						text: "Please make sure to read the text and tick the checkbox :(",
						timer: 1500,
						showCancelButton: false,
						showConfirmButton: false,
					});
				} else {
					console.log(`modal was dismissed by ${result.dismiss}`)
				}
			})
		},500);
	}
}
