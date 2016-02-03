/* Highlight current page in nav menu */
$(function(){
  $("a#nav").each(function(){
    if ($(this).prop("href") == window.location.href) {
      $(this).addClass("selected");
    };
  });
});

// Mobile nav menu
$(".menu").hide();
$("#menu-open").click(function() {
  $(".menu").toggle();
});

