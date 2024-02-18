$(document).ready(function(){
    $(".delete_from_cart").on("click", function(){
        var csrftoken = $('[name=csrfmiddlewaretoken]').val();
        var button = $(this)
        var product_id_ = button.attr("value")
        var api_url = $(this).attr("data-value-url")

        $.ajax({
            url: api_url,
            method: "POST",
            dataType: "json",
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: {product_id: product_id_},
            success: function(result) {
                var product_div = document.querySelector(`.product[data-product-id="${product_id_}"]`);

                if (product_div){
                    product_div.remove()
                } else {
                    location.reload();
                }
            }
        })
    })
})