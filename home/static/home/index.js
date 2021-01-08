$(document).ready(() => {
	console.log('index.js loaded');
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
});
