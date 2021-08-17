window.addEventListener("load", function () {
  $(document).ready(() => {
    console.log("datetime_field.js loaded");

    const startTime_date = $("#id_startTime_0");
    const startTime_time = $("#id_startTime_1");
    const endTime_time = $("#id_endTime_1");
    const registrationDeadline_time = $("#id_registrationDeadline_1");
    const cancellationDeadline_time = $("#id_cancellationDeadline_1");
    // Add event for inputs
    startTime_time.keyup(() => serialize(startTime_time));
    startTime_time.change(() => serialize(startTime_time));
    endTime_time.keyup(() => serialize(endTime_time));
    endTime_time.change(() => serialize(endTime_time));
    registrationDeadline_time.keyup(() => serialize(registrationDeadline_time));
    registrationDeadline_time.change(() =>
      serialize(registrationDeadline_time)
    );
    cancellationDeadline_time.keyup(() => serialize(cancellationDeadline_time));
    cancellationDeadline_time.change(() =>
      serialize(cancellationDeadline_time)
    );

    // Init serializer
    serialize(startTime_time);
    serialize(endTime_time);
    serialize(registrationDeadline_time);
    serialize(cancellationDeadline_time);

    const times = [
      startTime_time,
      endTime_time,
      registrationDeadline_time,
      cancellationDeadline_time,
    ];
    // Add events for "now" and "time chooser"
    setTimeout(() => {
      for (let i = 0; i < times.length; i++) {
        const now_btn = $("#" + times[i].attr("id") + " + span > a");
        now_btn.get(0).addEventListener("click", () => serialize(times[i]));
        $("#clocklink" + i).hide();
        if (i < 2) {
          $("#clocklink" + i)
            .parent()
            .get(0).style = "color: transparent;";
        } else {
          const extra_label = $("#clocklink" + i)
            .parent()
            .get(0);
          for (let j = 1; j <= 3; j++) {
            // X day before startTime
            const a = document.createElement("a");
            a.innerText = j + " day before startTime";
            a.href = "javascript:void(0)";
            a.addEventListener("click", function () {
              changeTime(j, i);
            });
            extra_label.appendChild(a);
            // Seperator
            const span = document.createElement("span");
            span.innerText = " | ";
            extra_label.appendChild(span);
          }
        }
      }
    }, 3000);
    const changeTime = function (minusDays, i) {
      const date = new Date(startTime_date.get(0).value);
      date.setDate(date.getDate() - minusDays);
      const month = "" + (date.getMonth() + 1);
      const day = "" + date.getDate();
      const new_date =
        date.getFullYear() +
        "-" +
        (month.length === 2 ? month : "0" + month) +
        "-" +
        (day.length === 2 ? day : "0" + day);
      $("#" + times[i].attr("id").replace("1", "0")).get(0).value = new_date;

      const time = startTime_time.get(0).value;
      times[i].get(0).value = time;
    };
  });
  const serialize = function (obj) {
    obj = obj.get(0);
    let tokens = obj.value.split(":").slice(0, 2);
    if (tokens[0] !== "" && tokens.length > 0) {
      tokens[0] = tokens[0].substring(0, 2);
      tokens[1] = tokens[1].substring(0, 2);
      obj.value = tokens[0] + ":" + tokens[1];
    }
  };
});
