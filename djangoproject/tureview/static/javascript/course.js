

$(document).ready(() => {

  setStars();

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

function setStars() {
  $('.whitebox').each(function(){
    // use $(this) to reference the current div in the loop
    let parent = $(this).find('#panel');
    let star = "<i class='fa fa-star'></i>";
    let starO = "<i class='fa fa-star-o'></i>";

    let infValue  = parent.find('#ratingInf-value').val();
    let ratingInf = parent.find('#ratingInf');
    let timeValue  = parent.find('#ratingTime-value').val();
    let ratingTime = parent.find('#ratingTime');
    let ReleValue  = parent.find('#ratingRele-value').val();
    let ratingRele = parent.find('#ratingRele');
    let DiffValue  = parent.find('#ratingDiff-value').val();
    let ratingDiff = parent.find('#ratingDiff');
    console.log("added stars");
    for (let i = 0; i < 5; i++) {
      if (i < infValue) {
        ratingInf.append(star);
      }
      else {
        ratingInf.append(starO);
      }
      if (i < timeValue) {
        ratingTime.append(star);
      }
      else {
        ratingTime.append(starO);
      }
      if (i < ReleValue) {
        ratingRele.append(star);
      }
      else {
        ratingRele.append(starO);
      }
      if (i < DiffValue) {
        ratingDiff.append(star);
      }
      else {
        ratingDiff.append(starO);
      }
    }
  });
}

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
