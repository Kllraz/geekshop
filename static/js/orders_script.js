window.onload = function () {
    let order_total_cost_el = $('.order_total_cost');
    let order_total_quantity_el = $('.order_total_quantity');
    let order_form_el = $('.order_form');

    let _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
    let quantity_arr = [];
    let price_arr = [];

    // let TOTAL_FORMS = parseInt($('input[name="orderitem-TOTAL_FORMS"]').val());

    let order_total_quantity = parseInt(order_total_quantity_el.text()) || 0;
    let order_total_cost = parseFloat(order_total_cost_el.text().replace(',', '.')) || 0;

    function TOTAL_FORMS() {
        return parseInt($('input[name="orderitem-TOTAL_FORMS"]').val());
    }

    function updateItemPrice() {
        $('.order_form select').change(function () {
            let target = event.target;
            orderitem_num = parseInt(target.name.replace('orderitem-', '').replace('-product', ''));

            let product_pk = target.options[target.selectedIndex].value;

            if (product_pk) {
                $.ajax({
                    url: `/orders/product/${product_pk}/price/`,
                    success: function (data) {
                        if (data.price) {
                            price_arr[orderitem_num] = parseFloat(data.price);
                            if (isNaN(quantity_arr[orderitem_num])) {
                                quantity_arr[orderitem_num] = 0;
                            }
                            let price_html = '<span class="order_total_cost">' +
                                data.price.toString().replace('.', ',') +
                                '</span>';
                            let current_tr = $('.order_form table').find(`tr:eq(${orderitem_num + 1})`);


                            current_tr.find('td:eq(2)').html(price_html);

                            if (isNaN(current_tr.find('input[type="number"]').val())) {
                                current_tr.find('input[type="number"]').val(0);
                            }
                            orderSummaryRecalc();
                        }
                    },
                });
            }
        });
    }

    function orderSummaryRecalc() {
        order_total_quantity = 0;
        order_total_cost = 0;

        for (let i = 0; i < TOTAL_FORMS(); i++) {
            order_total_quantity += quantity_arr[i];
            order_total_cost += quantity_arr[i] * price_arr[i];
        }
        order_total_quantity_el.html(order_total_quantity.toString());
        order_total_cost_el.html(Number(order_total_cost.toFixed(2)).toString());
    }

    updateItemPrice();

    for (let i = 0; i < TOTAL_FORMS(); i++) {
        _quantity = parseInt($(`input[name="orderitem-${i}-quantity"]`).val());
        _price = parseFloat($(`.orderitem-${i}-price`).text().replace(',', '.'));
        quantity_arr[i] = _quantity;
        if (_price) {
            price_arr[i] = _price;
        } else {
            price_arr[i] = 0;
        }
    }

    if (!order_total_quantity) {
        orderSummaryRecalc();
    }

    order_form_el.on('change', 'input[type="number"]', function () {
        let target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitem-', '').replace('-quantity', ''));
        if (price_arr[orderitem_num]) {
            orderitem_quantity = parseInt(target.value);
            delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
            quantity_arr[orderitem_num] = orderitem_quantity;
            orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        }
    });

    function orderSummaryUpdate(orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity;

        order_total_cost = order_total_cost + delta_cost;
        order_total_quantity = order_total_quantity + delta_quantity;

        order_total_cost_el.html(order_total_cost.toFixed(2));
        order_total_quantity_el.html(order_total_quantity);
    }

    function deleteOrderItem(row) {
        let target_name = row[0].querySelector('input[type="number"]').name;
        orderitem_num = parseInt(target_name.replace('orderitem-', '').replace('-quantity', ''));
        delta_quantity = -quantity_arr[orderitem_num];
        if (!isNaN(price_arr[orderitem_num] && !isNaN(delta_quantity))) {
            orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        }
    }

    $('.formset_row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить',
        prefix: 'orderitem',
        removed: deleteOrderItem,
        added: updateItemPrice,
    });
}