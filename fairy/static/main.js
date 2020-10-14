jQuery.noConflict();
jQuery(document).ready(function ($) {

  var arr = '';
  var ans = 1;
  $('.ch1, .ch2').click(function () {
    if (ans < 7) {
      arr += $(this).val();
      ans++;

      $.ajax({
        type: 'POST',
        url: '{% url "quest_data" %}',
        data: {
          num: ans,
          'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        dataType: "json",
        success: function (response) {
          $('.qst-num').html('Question ' + response.pk);
          $('.question').html(response.content);
          $('.ch1').html(response.answer1);
          $('.ch2').html(response.answer2);
        },
      });

      // $(this).parent().removeClass('select').addClass('notselect');
      // $(this).parent().next().removeClass('notselect').addClass('select');
    }
  });

  $('.result').click(function () {
    event.preventDefault()

    function post(params) {
      var form = $('form');

      $.each(params, function (key, value) {
        var field = $('<input>');

        field.attr("type", "hidden");
        field.attr("name", key);
        field.attr("value", value);

        form.append(field);
      });

      form.submit();
    }

    post({
      arr: arr
    });
  });
});