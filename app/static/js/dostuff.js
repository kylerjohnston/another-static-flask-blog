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

/* Add captions to images
 * Adapted from this stackoverflow post:
 * http://stackoverflow.com/questions/19331362/using-an-image-caption-in-markdown-jekyll
*/

(function addCaptionsToImages() {
  var images = document.getElementsByTagName('img');
  for (var i = 0; i < images.length; i++) {
    var caption = images[i].alt;
    var url = images[i].src;
    if (caption != '') {
      /*
       * <figure>
       *  <a href="{{ url }}"><img src=" {{ url }}" alt="{{ caption }}"></a>
       *  <figcaption>{{ caption }}</figcaption>
       * </figure>
       *
       */
      var parent = images[i].parentNode;
      var newFig = document.createElement('figure');
      var newLink = document.createElement('a');
      newLink.href = url;
      var newImg = document.createElement('img');
      newImg.src = url;
      newImg.alt = caption;
      newLink.appendChild(newImg);
      var newFigCaption = document.createElement('figcaption');
      newFigCaption.innerHTML = caption;
      newFig.appendChild(newLink);
      newFig.appendChild(newFigCaption);
      parent.replaceChild(newFig, images[i]);
    }
  }
})();

/* Add current date to copyright notice */

(function currentDateFooter() {
  var d = new Date();
  var dateElement = document.getElementById('current-year');
  var currentDate = document.createTextNode(d.getFullYear());
  dateElement.appendChild(currentDate);
})();

