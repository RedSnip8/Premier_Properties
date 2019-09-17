const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
  $('#message').fadeOut('slow');
}, 5000);

$('.card-link').hover(
  function(){ $(this).parents('div.card').addClass('card-link-active') },
  function(){ $(this).parents('div.card').removeClass('card-link-active') },
)