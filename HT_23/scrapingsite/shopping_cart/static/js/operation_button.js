$(document).ready(function(){
    var csrftoken = $('[name=csrfmiddlewaretoken]').val();

    $('button[name="operation"]').on('click', function(){
        var button = $(this)
        var value = button.attr("value");
        var api_url = $(this).attr("data-value-url")

        var [operation, product_id_] = value.split('|')

        $.ajax({
            url: api_url,
            method: "POST",
            dataType: "json",
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: {product_id: product_id_},
            success: function(result){
                var span_count_obj = document.querySelector(`.count_product[data-product-id="${product_id_}"]`);
                var count_span = parseInt(span_count_obj.textContent, 10);

                if (operation === "add") {
                    span_count_obj.textContent = count_span + 1
                } else {
                    span_count_obj.textContent = count_span - 1
                }

                var take_product_price = document.querySelector(`.price[data-product-id="${product_id_}"]`);
                var product_finish_price = document.querySelector(`.finish_price[data-product-id="${product_id_}"]`);

                product_finish_price.textContent = parseFloat(take_product_price.textContent) * parseInt(span_count_obj.textContent,10)

            }
        })
    })
})