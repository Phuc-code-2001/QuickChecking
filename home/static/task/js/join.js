$(document).ready(function(){

    $("#item_link").hide();
    $(".null_result").hide();

    $("#join_form").submit(function(e){
        e.preventDefault();
        k = $("input[name='q']").val();
        token = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({
            url: "",
            method: "POST",
            data: {
                key: k,
                csrfmiddlewaretoken: token
            },
            success: function(result){
                $("#item_link").attr('href', result.link);
                $("#owner").text(result.owner);
                $("#name").text(result.name);
                $("#date_opening").text(result.date_opening);
                $("#start_time").text(result.start_time);
                $("#end_time").text(result.end_time);
                $("#item_link").show();
                $(".null_result").hide();
            },
            error: function(result){
                $(".null_result").text(result.responseText);
                $(".null_result").show();
                $("#item_link").hide();
            }
        });

    });

});