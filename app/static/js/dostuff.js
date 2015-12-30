$(function(){
  $("a#nav").each(function(){
    if ($(this).prop("href") == window.location.href) {
      $(this).addClass("selected");
    };
  });
});
