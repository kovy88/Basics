(function($){
    $(function(){
        $(".jqScLoc").click(function(){
            $("html, body").animate({scrollTop: $(".jqLoc").offset().top}, 800)
        });
        $(".jqScOff").click(function(){
            $("html, body").animate({scrollTop: $(".jqOff").offset().top}, 800)
        });
        $(".jqScRef").click(function(){
            $("html, body").animate({scrollTop: $(".jqRef").offset().top}, 800)
        });
        $(".jqScFoto").click(function(){
            $("html, body").animate({scrollTop: $(".jqFoto").offset().top}, 800)
        });
        $(".jqScAsk").click(function(){
            $("html, body").animate({scrollTop: $(".jqAsk").offset().top}, 800)
        });

        $(".jqnavicon").click(function(){
            $(".nav_background").slideToggle();
            $(".mobile_nav_back").slideToggle();
            $("nav ul").slideToggle();   
        });
        
        $(".jqicon").click(function(){
            if ($(".jqicon").attr("src") == "img/hamburgerMenu.png") {
                
                $( $(".jqicon").attr("src", "img/crossMenu.png"));
            } 
            else {
                $( $(".jqicon").attr("src", "img/hamburgerMenu.png"));
            }
        });
        

    });
})(jQuery);

