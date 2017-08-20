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





//the last row of artboxes is adjusted if there are not three boxes to fill the cols
//1 box -> gets col-md-12
//2 boxes -> each get col-md-6
var boxes = $(".handmadeCrop");

var boxesLeft = boxes.length % 3;

if(boxesLeft == 2){
    //we are centering two boxes with col-md-6

    cols = $(".col-md-4").slice(-2);

    cols.each(function(){
        $(this).removeClass('col-md-4').addClass('col-md-6');
        $(this).find(".handmadeCrop").addClass('pull-right');
    });

    cols.last().find(".handmadeCrop").removeClass('pull-right').addClass('pull-left');

}else if(boxesLeft ==1){
    //we are centering 1 box with col-md-12
    //:last or last()
    $(".col-md-4").slice(-1).removeClass('col-md-4').addClass('col-md-12');
    $(".col-md-12 .handmadeCrop").slice(-1).addClass('center-block');

}





//for centering the image nicely
//Y axis is not 100% centered- tried out that art thing where you leave more space below
$("img").ready(function(){
    $(".cardImg").each(function(){

        //$(this).css('visibility','hidden');

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
        $(this).css('visibility', 'visible');

    })
});