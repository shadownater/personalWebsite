/**
 * Created by Jill - Offline on 2017-07-25.
 */


$( ".handmadeCrop" ).hover(
  function() {

      $(this).find("h4").slideDown( "fast", function() {
    // Animation complete.
          console.log("I ran.");
    });

    console.log("You got me");
  }, function() {

      $(this).find("h4").css("display", "none");

    console.log("Now Im gone");
  }
);
