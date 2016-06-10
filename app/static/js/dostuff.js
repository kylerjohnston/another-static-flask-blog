// Check for jQuery
if(typeof jQuery === 'undefined') {
  document.write(unescape("%3Cscript src='/static/js/jquery-2.2.0.min.js' type='text/javascript'%3E%3C/script%3E"));
};

/* Highlight current page in nav menu */
(function highlightCurrentPage() {
  var nav = document.getElementsByClassName('nav');
  for (var i = 0; i < nav.length; i++) {
    if (nav[i].href == window.location.href) {
      nav[i].className += ' selected';
    };
  }
})();

/* Hide/show mobile nav menu */
(function hideShowMobileNav() {
  var menu = document.getElementsByClassName('menu');
  var menuOpen = document.getElementById('menu-open');
  var menuClose = document.getElementById('menu-close');
  menuClose.style.display = 'none';
  menu[0].style.display = 'none';
  menuOpen.addEventListener('click', function(event) {
    menu[0].style.display = 'block';
    menuClose.style.display = 'block';
    menuOpen.style.display = 'none';
  });
  menuClose.addEventListener('click', function(event) {
    menu[0].style.display = 'none';
    menuClose.style.display = 'none';
    menuOpen.style.display = 'block';
  });
})();

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
