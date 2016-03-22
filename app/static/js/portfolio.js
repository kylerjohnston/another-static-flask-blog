// Check for jQuery
if(typeof jQuery === 'undefined') {
  document.write(unescape("%3Cscript src='/static/js/jquery-2.2.0.min.js' type='text/javascript'%3E%3C/script%3E"));
};

// Mobile nav menu
var open = '<i class="fa fa-bars"></i>';
var close = '<i class="fa fa-times"></i>';
$(function() {
  if ($(window).width() <= 800) {
    $(".nav-menu").hide();
    $(".sticky").hide()
  }
  $("#menu-open").click(function() {
    $(".nav-menu").toggle();
    if ($("#menu-open").html() === open) {
      $("#menu-open").html(close);
    }
    else {
      $("#menu-open").html(open);
    }
  });
});

$(".nav").click(function() {
  if ($(window).width() <= 800) {
    $(".nav-menu").hide();
    $("#menu-open").html(open);
  }
});

// sticky header

$(window).scroll(function() {
  if($("#nav-menu").is(":visible")) {
    var y = $(this).scrollTop();
    if (y >= $("#projects").offset().top - 60) {
      $("#nav-menu").removeClass("nav-menu");
      $("#nav-menu").addClass("sticky");
    }
    else {
      $("#nav-menu").removeClass("sticky");
      $("#nav-menu").addClass("nav-menu");
    }
    $('.nav').each(function (event) {
      if (y >= $($(this).attr('href')).offset().top - 40) {
        $('.nav').not(this).removeClass('selected');
        $(this).addClass('selected');
      }
    });
  }
});
