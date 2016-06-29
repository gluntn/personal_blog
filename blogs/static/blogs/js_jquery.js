$(document).ready(function() { });

  var loc = window.location.pathname;

   $('#menu li').find('a').each(function() {
     $(this).toggleClass('active', $(this).attr('href') == loc);
  });
