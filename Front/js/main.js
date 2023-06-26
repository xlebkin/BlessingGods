;(function($) {
'use strict'

$('a[name=scrollTo]').on('click', function() {

    let href = $(this).attr('href');

    $('html, body').animate({
        scrollTop: $(href).offset().top - 90
    }, {
        duration: 450, 
        easing: "linear"
    });

    return false;
});

$('.start-button a').on({
    mouseenter: function () {
        $('.start-button img').css('transform', 'translate(0,10px)');
    },
    mouseleave: function () {
        $('.start-button img').css('transform', 'translate(0,0)');
    }
});

$('#posts .posts__item').on('click', function(e) {
    e.preventDefault();
    window.location.href = "post.html";
});

})(jQuery);