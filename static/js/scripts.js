
// Closes responsive menu when a scroll trigger link is clicked
$('.js-scroll-trigger').click(function () {
    $('.navbar-collapse').collapse('hide');
    $('#mainNav').css("background-color", "transparent");
});


// Add JQuery event for mainNav background color:
$('.navbar-toggler').click(function () {
    $("#mainNav").css("background-color", "gray");
});


// This function highligth current page
$(function () {
    $('li a').each(function () {
        if ($(this).prop('href') == window.location.href) {
            $(this).addClass('active'); $(this).parents('li').addClass('active');
        }
    });
});


$("form[name=signup_form]").submit(function (e) {

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

/*
$("form[name=subscribe_form]").submit(function (e) {
        e.preventDefault();
        var $form = $(this);
        var data = $form.serialize();
        var $error = $form.find("p")
        $.ajax({
            type : 'POST',
            data: data,
            dataType: "json",
            url : "/",
            success : function(resp){
            
            },
            error: function (resp) {
            $error.css("color", "red");
        }
        });
        return false;
    });
*/