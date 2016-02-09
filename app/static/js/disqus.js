var disqus_config = function () {
  var w = window.location.href;
  this.page.url = w; // Replace PAGE_URL with your page's canonical URL variable
  this.page.identifier = w.split("/")[w.split("/").length-2]; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
(function() { // DON'T EDIT BELOW THIS LINE
  var d = document, s = d.createElement('script');

  s.src = '//kylerjohnston.disqus.com/embed.js';

  s.setAttribute('data-timestamp', +new Date());
  (d.head || d.body).appendChild(s);
})();

