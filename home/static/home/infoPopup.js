$(document).ready(() => {
  console.log("infoPopup.js loaded");
  const info = $("#infoPopup");
  const btn = $("#infoPopupBtn");
  const chkbox = $("#infoPopupChkbox").get(0);
  if (
    !sessionStorage["hideInfoOnSession"] &&
    !localStorage["hideInfoOnSession"]
  ) {
    info.addClass("visible");
    setTimeout(() => {
      hidePopup(info, chkbox.checked);
    }, 25000);
  }
  btn.on("click", (e) => {
    e.preventDefault();
    hidePopup(info, chkbox.checked);
  });
});
const hidePopup = (info, bool) => {
  info.removeClass("visible");
  sessionStorage["hideInfoOnSession"] = true;
  if (bool) {
    localStorage["hideInfoOnSession"] = true;
  }
};
