window.onload = function () {
    $('.basket_list').on('change', 'input[type="number"]', function () {
        let target = event.target;

        $.ajax({
            url: `/basket/edit/${target.name}/${target.value}/`,
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });

        event.preventDefault();
    });
}