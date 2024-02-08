$(document).ready(function() {

    $(".url_button").on("click", function() {
        var button = $(this)
        
        var product_id_ = $(this).attr("data-product-id")
        var csrftoken = $('[name=csrfmiddlewaretoken]').val();

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
                if (result.InCart === true) {
                    button.css("background", "green");
                } else {
                    button.css("background", "lightgrey");
                }
            },
        })
    })

})