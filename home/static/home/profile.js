$(document).ready(() => {
	console.log('profile.js loaded');
	const nav = $(".divbox.nav").children().get();
	const displays = $(".profile_display").get();
	for (let i = 0; i < nav.length; i++) {
		$(nav[i]).click(() => navigate(i,displays));
	}
	// Hides all other displays other than profile
	for (let i = 1; i < displays.length; i++) {
		$(displays[i]).hide();
	}

	// temp
	// $(displays[0]).hide();
	// $(displays[1]).show();
});

const navigate = (i,displays) => {
	console.log(i,displays[i]);
	for (let j = 0; j < displays.length; j++) {
		if (i == j) {
			$(displays[j]).show('slow');
		} else {
			$(displays[j]).hide('slow');
		}
	}
}
