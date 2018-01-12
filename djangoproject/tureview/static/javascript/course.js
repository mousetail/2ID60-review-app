$(document).ready(() => {

  $('#thumbsUp').on('click', () => {
    console.log('Thumbs Up button clicked');
    thumbs('up');
  });

  $('#thumbsDown').on('click', () => {
    console.log('Thumbs Up button clicked');
    thumbs('down');
  });

});


function thumbs(upDown) {

  $.ajax(window.location.href + 'thumbs',
      {"method":"POST",
      data : {
             "thumbs": upDown,
             }
      });
}
