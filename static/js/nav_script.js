$(document).ready(function (){
    $.ajax({
        url: '/products/update-nav/',
        success: function (data) {
            $('nav.fixed-top').html(data.result);
        },
    });
});

$(".add-product").on('click', function (){
    $.ajax({
        url: '/products/update-basket/',
        success: function (data) {
            $('.total_cost').html(`${data.result.replace('.', ',')}&nbsp;руб.`);
        },
    });
})