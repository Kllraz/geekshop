window.onload = function () {
    let basket = $('.basket_list');

    basket.on('change', 'input[type="number"]', function () {
        let target = event.target;

        $.ajax({
            url: `/basket/edit/${target.name}/${target.value}/`,
            success: function (data) {
                basket.html(data.result);
            }
        });

        event.preventDefault();
    });

    basket.on('click', '.remove-product', function () {
        let target = event.target;

        $.ajax({
            url: `/basket/remove-product/${target.getAttribute('data-id')}/`,
            success: function (data) {
                basket.html(data.result);
            }
        });

        event.preventDefault();
    });

    $('.add-product').on('click', function () {
        let target = event.target;

        $.ajax({
            url: `/basket/add-product/${target.getAttribute('data-id')}/`,
        });
    });
}