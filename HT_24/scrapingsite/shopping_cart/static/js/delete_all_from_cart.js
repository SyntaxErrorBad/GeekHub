$(document).ready(function(){

    var csrftoken = $('[name=csrfmiddlewaretoken]').val();

    $("#clear_cart").on("click", function(){
        var url_api = $(this).attr("data-value-url")
        $.ajax({
            url: url_api,
            method: "POST",
            dataType: "json",
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(result) {
                $(".product").remove()
            }
        })
    })
})