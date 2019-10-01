const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
  $('#message').fadeOut('slow');
}, 5000);

$('.card-link').hover(
  function(){ $(this).parents('div.card').addClass('card-link-active') },
  function(){ $(this).parents('div.card').removeClass('card-link-active') },
)

function bootstrapClearButton() {
  $('.position-relative :input').on('keydown focus', function() {
    if ($(this).val().length > 0) {
      $(this).nextAll('.form-clear').removeClass('d-none');
    }
  }).on('keydown keyup blur', function() {
    if ($(this).val().length === 0) {
      $(this).nextAll('.form-clear').addClass('d-none');
    }
  });
  $('.form-clear').on('click', function() {
    $(this).addClass('d-none').prevAll(':input').val('');
  });
}

bootstrapClearButton();