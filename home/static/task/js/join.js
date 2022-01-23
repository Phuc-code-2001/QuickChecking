$(document).ready(function(){

    $(".item_result").hide();
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
                $(".item_result").show();
                $(".null_result").hide();
            },
            error: function(result){
                let text = `${result.statusText}. `;
                if(result.status == 500) text += "Try again after a few seconds."
                else text += "Please check the key.";
                $(".null_result").text(text);
                $(".null_result").show();
                $(".item_result").hide();
            }
        });

    });

});