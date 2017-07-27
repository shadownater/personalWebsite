/**
 * Created by Jill - Offline on 2017-07-25.
 */

//for the cool neato way the title shows on hover
$( ".handmadeCrop" ).hover(
  function() {

      //this is on-hover
      $(this).find("h4").slideDown( "fast", function() {
    // Animation complete. Callback function.
    });

  }, function() {
      //this is when hover ends
      $(this).find("h4").css("display", "none");


  }
);



//for centering the image nicely
//Y axis is not 100% centered- tried out that art thing where you leave more space below
$(".cardImg").each(function(){

    var img_width = $(this).width();
    var img_height = $(this).height();
    var clippingBoxW = $(".handmadeCrop").width();
    var clippingBoxH = $(".handmadeCrop").height();

    //centers of both the image itself and the clipping box
    var centeringW = img_width/2.0;
    var centeringH = img_height/2.0;
    var clippingCenterW = clippingBoxW/2.0;
    var clippingCenterH = clippingBoxH/2.0;

    centeringW -= clippingCenterW;
    centeringH = centeringH - clippingCenterH + (clippingCenterH/5);

    centeringW *=(-1);
    centeringH *=(-1);

    $(this).css('margin-left', centeringW);
    $(this).css('margin-top', centeringH);

});

//css({'margin-top':'300px'});