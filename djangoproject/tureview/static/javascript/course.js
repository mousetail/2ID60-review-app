

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

  /*$("div").siblings("#flip").click(function(){
      $(this).siblings().slideToggle();
      console.log("flip");
  });*/

  //$("div").siblings("#flip").siblings().hide();

  $('.showMore').on('click', event => {
    console.log('Show more');
    showMore(event);
  });

  $('.showLess').on('click', event => {
    console.log('Show less');
    showLess(event);
  });

});

function thumbs(upDown, event) {
  let thumbsUp = $(event.currentTarget).siblings('#thumbsUpCount');
  let thumbsDown = $(event.currentTarget).siblings('#thumbsDownCount');
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
  console.log(review_pk)

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

function showMore(event) {
  let downButton = $(event.currentTarget);
  let upButton = $(event.currentTarget).siblings('.showLess');
  let text = $(event.currentTarget).parents('#flip').siblings('#panel');
  downButton.hide();
  upButton.show();
  text.fadeIn();
}

function showLess(event) {
  let upButton = $(event.currentTarget);
  let downButton = $(event.currentTarget).siblings('.showMore');
  let text = $(event.currentTarget).parents('#flip').siblings('#panel');
  downButton.show();
  upButton.hide();
  text.fadeOut(200);
}
