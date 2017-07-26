/**
 * Created by Jill - Offline on 2017-07-25.
 */


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
