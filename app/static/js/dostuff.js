// Check for jQuery
if(typeof jQuery === 'undefined') {
  document.write(unescape("%3Cscript src='/static/js/jquery-2.2.0.min.js' type='text/javascript'%3E%3C/script%3E"));
};

/* Highlight current page in nav menu */
$(function(){
  $("a#nav").each(function(){
    console.log('this.href: ' + $(this).prop("href"));
    console.log('window.location.href: ' + window.location.href);
    if ($(this).prop("href") == window.location.href) {
      $(this).addClass("selected");
    }
    else if ($(this).prop("href") == "/" && window.location.href == "/index.html") {
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
      $(this).replaceWith('<figure><a href="' + url + '"><img src="' + url + '" alt="' + caption + '"></a><figcaption>' + caption + '</figcaption></figure>');
    }
  });
});

// Add current date to copyright notice
$(function() {
  var d = new Date();
  $('span#current-year').replaceWith(d.getFullYear());
});
