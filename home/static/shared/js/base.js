
$(document).ready(function(){

    let ShowControl = function() {
        $(".page_control").css("transform", "none");
    }

    let HideControl = function() {
        $(".page_control").css("transform", "translateX(-100%)");
    }

    $(".control_toggle_button").click(function(){

        if($(".page_control").css("transform") == "none"){
            HideControl();
        }
        else {
            ShowControl();
        }

    });

    $(window).resize(function(){
        if($(this).outerWidth() >= 600){
            ShowControl();
        }
        else {
            HideControl();
        }
    })

});