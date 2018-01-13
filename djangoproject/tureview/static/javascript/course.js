$(document).ready(() => {

  $('.thumbsUp').on('click', event => {
    // console.log('Thumbs Up button clicked');
    let value = $('#review-pk').val();
    thumbs('up', event);
  });

  $('.thumbsDown').on('click', event => {
    // console.log('Thumbs Up button clicked');
    thumbs('down', event);
  });

  $("div").siblings("#flip").click(function(){
      $(this).siblings().slideToggle();
      console.log("flip");
  });

  $("div").siblings("#flip").siblings().hide();

});

function thumbs(upDown, event) {
  let thumbsUp = $(event.currentTarget).siblings('#thumbsUpText').children('#thumbsUpCount');
  let thumbsDown = $(event.currentTarget).siblings('#thumbsDownText').children('#thumbsDownCount');
  let review_pk = $(event.currentTarget).siblings('#review-pk').val();
  let active = $(event.currentTarget).children('.active');
  let inactive = $(event.currentTarget).children('.inactive');
  let other_active;
  let other_inactive;
  if (upDown == 'up') {
    other_active = $(event.currentTarget).siblings('#thumbsDown').children('.active');
    other_inactive = $(event.currentTarget).siblings('#thumbsDown').children('.inactive');
  }
  else {
    other_active = $(event.currentTarget).siblings('#thumbsUp').children('.active');
    other_inactive = $(event.currentTarget).siblings('#thumbsUp').children('.inactive');
  }


  $.ajax({
    url: window.location.href + 'thumbs/',
    type: 'POST',
    dataType: 'json',
    data : {
      "thumbs": upDown,
      "review_pk": review_pk
    },
    success(response) {
      thumbsUp.text(response.up);
      thumbsDown.text(response.down);
      console.log(response.state);
      if (response.state == 'none') { // Deactivate thumb
        active.hide();
        inactive.show();
      }
      else { // Activate thumb
        inactive.hide();
        active.show();
      }
      other_active.hide(); // Deactivate other thumbs
      other_inactive.show();
    },
    error(jqXHR, status, errorThrown) {
      console.log("error");
      console.log(jqXHR);

    }
  });
}
