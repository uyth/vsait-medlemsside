var $ = django.jQuery;
$(document).ready(() => {
  console.log("draft.js loaded");

  // Draft show/hide draft_publish_time
  const is_draft = $("#id_is_draft");
  const draft_publish_time = $(".field-draft_publish_time");
  // Default state
  if (!is_draft.is(":checked")) draft_publish_time.hide();

  // Onchange of checkbox, shows/hides time
  is_draft.change(() => {
    if (is_draft.is(":checked")) {
      draft_publish_time.show("slow");
    } else {
      draft_publish_time.hide("slow");
    }
  });
});
