// Here I include JQuery function to include some animation on pages

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

