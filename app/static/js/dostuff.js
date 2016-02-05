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

// Add captions to images
// Adapted from this stackoverflow post:
// http://stackoverflow.com/questions/19331362/using-an-image-caption-in-markdown-jekyll
$(function() {
  var caption;
  $('img').each(function() {
    caption = $(this).attr('alt');
    url = $(this).attr('src');
    if(caption != '') {
      $(this).replaceWith('<figure><img src="' + url + '" alt="' + caption + '"><figcaption>' + caption + '</figcaption></figure>');
    }
  });
});

// Add current date to copyright notice
$(function() {
  var d = new Date();
  $('span#current-year').replaceWith(d.getFullYear());
});
