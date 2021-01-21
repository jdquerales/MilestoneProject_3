
// Closes responsive menu when a scroll trigger link is clicked
$('.js-scroll-trigger').click(function () {
    $('.navbar-collapse').collapse('hide');
});

$("form[name=signup_form").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error")
    var data = $form.serialize();

    $.ajax({
        url: "/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/dashboard"
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});

$("form[name=login_form").submit(function (e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/signin",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (resp) {
            window.location.href = "/dashboard";
        },
        error: function (resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});