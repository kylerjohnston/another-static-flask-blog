var primaryBlue = "#3080e8";
var darkGrey = "#424242";

var navOpen = document.getElementById("nav-open");
var navClose = document.getElementById("nav-close");
var mobileNav = document.getElementById("mobile-nav");

// This function turns the header link arrows in the Projects section
// blue on mouse hover.
(function() {
  var links = document.getElementsByClassName("header-link");
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener("mouseover", function(event) {
      this.children[0].style.color = primaryBlue;
    });
    links[i].addEventListener("mouseout", function(event) {
      this.children[0].style.color = darkGrey;
    });
  }
})();

// This function works the mobile nav menu
(function() {
  var about = document.getElementById("about");
  window.addEventListener("scroll", function(event) {
    if (window.scrollY < about.offsetTop && navClose.style.display != "block") {
      navOpen.style.display = "none"
    }
    else if (window.scrollY >= about.offsetTop && navClose.style.display != "block") {
      navOpen.style.display = "block";
    }
  });
  function closeMenu() {
    navOpen.style.display = "block";
    mobileNav.style.display = "none";
    navClose.style.display = "none";
  }
  var mobileLinks = document.getElementsByClassName("mobile-link");
  for (var i = 0; i < mobileLinks.length; i++) {
    mobileLinks[i].addEventListener("click", closeMenu);
  }
  navOpen.addEventListener("click", function(event) {
    navClose.style.display = "block";
    mobileNav.style.display = "block";
    this.style.display = "none";
  });
  navClose.addEventListener("click", closeMenu);
})();
