$(document).ready(function (){
    $.ajax({
        url: 'update-nav/',
        success: function (data) {
            $('nav').html(data.result);
        },
    });
});

$(".add-product").on('click', function (){
    $.ajax({
        url: 'update-basket/',
        success: function (data) {
            $('.total_cost').html(data.result);
        },
    });
})