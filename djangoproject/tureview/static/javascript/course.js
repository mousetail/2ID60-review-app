$(document).ready(() => {

  $('.thumbsUp').on('click', () => {
    console.log('Thumbs Up button clicked');
    let value = $('#review-pk').val();
    thumbs('up');
  });

  $('.thumbsDown').on('click', () => {
    console.log('Thumbs Up button clicked');
    thumbs('down');
  });

});


function thumbs(upDown) {
  let review_pk = 
  console.log("review_pk: " +
  $.ajax({
      url: window.location.href + 'thumbs/',
      type: 'POST',
      dataType: 'json',
      data : {
             "thumbs": upDown,
             "review_pk": $('#review-pk').val()
           },
      success(response) {
        console.log('response: ' + response.state);
      },
      error(jqXHR, status, errorThrown) {
        console.log("error");
        console.log(jqXHR);

      }
  });
}
