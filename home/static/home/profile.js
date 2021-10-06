$(document).ready(() => {
  console.log("profile.js loaded");
  // registration form
  const foodBtn = $("#food").get(0);
  const passwordBtn = $("#password").get(0);
  const membershipBtn = $("#membership").get(0);
  if ($("#alert").get(0)) {
    // Alert message after password change found
    const alert = $("#alert").get(0);
    $(alert).hide();
    const alertInfo = {};
    if (alert.className === "success") {
      alertInfo.title = "Success!";
      alertInfo.text = "Du har endret ditt passord!";
      alertInfo.icon = "success";
    } else {
      alertInfo.title = "Error!";
      alertInfo.text = "Se og fiks feilmeldingene nedenfor!";
      alertInfo.icon = "error";
    }
    Swal.fire({
      title: alertInfo.title,
      text: alertInfo.text,
      icon: alertInfo.icon,
      timer: 1500,
      showCancelButton: false,
      showConfirmButton: false,
    });
  }
  $(foodBtn).on("click", click);
  $(passwordBtn).on("click", click2);
  $(membershipBtn).on("click", click3);
  $("input").blur();
});

const click = function (e) {
  e.preventDefault();
  const form = $($(this).parents("form").get(0));
  console.log(form);
  const alertInfo = getInfo(this.id);
  Swal.fire({
    title: alertInfo.title,
    text: alertInfo.text,
    icon: alertInfo.icon,
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: alertInfo.confirmButtonText,
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: alertInfo.s_title,
        text: alertInfo.s_text,
        icon: "success",
        timer: 1500,
        showCancelButton: false,
        showConfirmButton: false,
      }).then(function () {
        form.submit();
      });
    }
  });
};
const click2 = function (e) {
  e.preventDefault();
  const form = $($(this).parents("form").get(0));
  const alertInfo = getInfo(this.id);
  Swal.fire({
    title: alertInfo.title,
    text: alertInfo.text,
    icon: alertInfo.icon,
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: alertInfo.confirmButtonText,
  }).then((result) => {
    if (result.isConfirmed) {
      form.submit();
    }
  });
};
const click3 = function (e) {
  e.preventDefault();
  const form = $($(this).parents("form").get(0));
  const alertInfo = getInfo(this.id);
  Swal.fire({
    title: "BLI MEDLEM",
    html: 'Medlemskontingenten kan betales via nettbank eller Vipps.<br/><br/>Via nettbank betaler du ved å overføre 100 kroner til kontonummer 4212.13.37740 eller IBAN NO1742121337740. Skriv navnet ditt i blanketten.<br/><br/>På Vipps, gå inn på "Send" og søk "VSAiT". Velg “Medlemsavgift/Membership fee”. Dersom navnet ditt på Vipps er forskjellig fra hva du registrerer deg med her, skriv en kommentar med navnet du vanligvis bruker',
    icon: alertInfo.icon,
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Ok",
    cancelButtonText: "Avbryt",
    input: "checkbox",
    inputPlaceholder: "Jeg bekrefter at jeg har betalt",
  }).then(function (result) {
    if (result.value) {
      Swal.fire({
        icon: "success",
        text: "Vellykket registrering! Vi oppdaterer medlemsskapet ditt når vi har mottat betaling.",
        showCancelButton: false,
        showConfirmButton: true,
        confirmButtonText: "Ok",
      }).then(function () {
        form.submit();
      });
    } else if (result.value === 0) {
      Swal.fire({
        icon: "error",
        text: "Vennligst les teksten og huk av avmerkingsboksen!",
        timer: 2500,
        showCancelButton: false,
        showConfirmButton: false,
      });
    } else {
      console.log(`modal was dismissed by ${result.dismiss}`);
    }
  });
};
const getInfo = function (id) {
  console.log(id);
  const info = {};
  if (id === "food") {
    info.title = "Are you sure?";
    info.text = "Du endrer nå ditt matbehov.";
    info.icon = "warning";
    info.confirmButtonText = "Yes!";
    // success
    info.s_title = "Endret!";
    info.s_text = "Du har endret ditt matbehov!";
  } else if (id === "password") {
    info.title = "Are you sure?";
    info.text = "Du endrer nå ditt passord.";
    info.icon = "warning";
    info.confirmButtonText = "Yes!";
  }
  return info;
};
