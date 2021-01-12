$(document).ready(() => {
	console.log('signup.js loaded');
	registration_alert();
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
