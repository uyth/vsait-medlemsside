$(document).ready(() => {
  console.log("index.js loaded");
  membership_alert();
  confirmEmail_alert();
  no_account_alert();
  // Show password
  const show_password = $(".show_password a");
  show_password.on("click", function () {
    const input_password = $(this).parent().siblings().get(0);
    input_password.type =
      input_password.type === "password" ? "text" : "password";
    show_password.get(0).innerText =
      input_password.type === "password" ? "Vis" : "Skjul";
  });

  $("#cbtn").on("click", function (e) {
    e.preventDefault();
    $.ajax({
      type: "post",
      data: $("#cform").serialize(),
    }).done(function () {
      console.log("sent confirmation");
      calert();
    });
    return false;
  });
});

const no_account_alert = function () {
  const alert = $("p.error").get(0);
  if (alert) {
    Swal.fire({
      title: "Bruker ikke funnet!",
      html: "Kombinasjonen av eposten og passordet du har oppgitt er feil. Kontroller eposten og passordet, og prøv på nytt.",
      icon: "error",
      showCancelButton: false,
      confirmButtonColor: "#3085d6",
      confirmButtonText: "Ok",
    });
  }
};

const send_confirmation = () => {
  const email_inp = $("#id_email").get(0);
  const cbtn = $("#cbtn").get(0);
  $("#id_user").get(0).value = email_inp.value;
  setTimeout(() => cbtn.click(), 500);
};
const calert = function () {
  Swal.fire({
    title: "Du må aktivere brukeren først!",
    html: "Du har fått tilsendt epost om å aktivere VSAiT brukeren din. Du må bekrefte eposten før du kan logge inn.<br/>Har ikke fått noe mail?<br/><a href='javascript:send_confirmation()'>Trykk her for å sende på nytt.</a>",
    icon: "error",
    showCancelButton: false,
    confirmButtonColor: "#3085d6",
    confirmButtonText: "Ok",
  });
};
const confirmEmail_alert = function () {
  const alert = $("p.warning").get(0);
  if (alert) calert();
};

const membership_alert = function () {
  const alert = $("#alert_not_read").get(0);
  if (alert) {
    const form = $($(alert).parents("form").get(0));
    setTimeout(() => {
      Swal.fire({
        title: "Husk å bli medlem!",
        html: "Som medlem kan du bli med på arrangementer<br/>Bli medlem ved å gå inn på din profil!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Ok",
        cancelButtonText: "Avbryt",
        input: "checkbox",
        inputPlaceholder: "Jeg har lest.",
      }).then(function (result) {
        if (result.value) {
          Swal.fire({
            icon: "success",
            text: "Denne meldingen vil ikke vises igjen",
            timer: 2000,
            showCancelButton: false,
            showConfirmButton: false,
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
    }, 500);
  }
};
