;(function($) {
    'use strict'
    $(document).ready(function(){
        $('.slider').slick({
            dots: false,
            arrows: false,
            infinite: true,
            autoplay:true,
            speed:1500,
            autoplaySpeed:1500,
            slidesToShow: 1
        });
    });
})(jQuery);