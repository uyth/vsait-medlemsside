$(document).ready(() => {
	console.log('signup.js loaded');
	registration_alert();

	// Show password
	// Create show_passord buttons, and add event on click
	const password_inp = $("#id_password").get(0);
	const password_confirmation_inp = $("#id_password_confirmation").get(0);
	for (const input of [password_inp, password_confirmation_inp]) {
		const div = document.createElement("div");
		div.className = "show_password";
		const show_password = document.createElement("a");
		show_password.innerText = "Vis";
		show_password.href = "javascript:void(0)";
		$(show_password).on('click',function() {
			const input_password = input;
			input_password.type = (input_password.type === "password") ? "text" : "password";
			this.innerText = (input_password.type === "password") ? "Vis" : "Skjul";
		});
		div.appendChild(show_password);
		$(input).parent().get(0).appendChild(div);
	}
});
const registration_alert = function() {
	const alert = $("p.success").get(0);
	if (alert) {
		Swal.fire({
			title: "Velkommen til VSAIT!",
			html: "Du har blitt sent en mail om å aktivere brukeren.<br/>Har ikke fått noe mail? Sjekk søppelposten din!<br/><a href='javascript:void(0)'>Trykk her ellers for å sende på nytt.</a>",
			icon: "success",
			showCancelButton: false,
			confirmButtonColor: '#3085d6',
			confirmButtonText: "OK.",
		}).then(function() {
			window.location.replace("http://"+window.location.host+"/");
		})
	}
}
