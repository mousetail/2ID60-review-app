/* uitklapfunctie voor form*/
$(document).ready(function() {
        $(".text").hide();
        $(".expand").click(function() {
                $(this).next(".text").slideToggle(500);
                $(this).text($(this).text() == 'Less filters' ? 'More filters' : 'Less filters').toggleClass('up');
        });
});


$("#searchform").on("submit", function(ev) {
    ev.preventDefault();
    var value = $("#idfield").val();
    if (value.length > 4){
        window.location = "/course/"+value;
    }
    else {
        $.ajax("/api/search",
            {"method":"POST",
            data : {
                   "year": $("#yearfield").val(),
                   "fac": $("#facfield").val(),
                   "name": $("#namefield").val(),
                   "slot": $("#timeslotfield").val(),
                   "quartile": $("#quartilefield").val(),
                   "minRating": $("#minratingfield").val(),
                   "sort": $("#sortfield").val()
                   }
            }).done(
                function(data) {
                    var itm = $("#result");
                    itm.empty();
                    console.log(data);
                    if (data.length==0) {
                      console.log("POEP");
                      $("#noresults", copy).text("No results :(");
                    }
                    else {
                      for (var index in data){
                        $("#noresults", copy).text("");
                          var copy = $("#courseTemplate").clone();
                          $(copy).css("display", "")
                          $(copy).attr("id", "cTemplate"+index)
                          $("#cID", copy).text(data[index].id);
                          $("#link", copy).attr("href", "/course/"+data[index].id)
                          $("#cName", copy).text(data[index].name);
                          $("#cShortDesc", copy).text(data[index].shortDesc);
                          $("#cLongDesc", copy).text(data[index].longDesc);
                          if (Number(data[index].numReviews) > 0){
                              $("#cAvgRat", copy).text(data[index].avgRating);
                            if (Number(data[index].numReviews) > 1){
                              $("#aReview", copy).text(data[index].numReviews+" reviews");
                            }
                            else {
                              $("#aReview", copy).text(data[index].numReviews+" review");
                            }
                          }
                          else {
                              $("#cAvgRat", copy).text("-")
                              $("#aReview", copy).text("0 reviews");
                          }

                          for (var year in data[index].years){
                              var yearCopy = $("#yearTemplate").clone();
                              $(yearCopy).css("display","");
                              $(yearCopy).attr("id", "yTemplate"+index+"y"+year);
                              $("#yName", yearCopy).text(year+": ");

                              for (var quartile in data[index].years[year]){
                                  var qCopy = $("#quartileTemplate").clone();
                                  $(qCopy).css("display","");
                                  $(qCopy).attr("id", "qTemplate"+index+"y"+year+"q"+quartile);

                                  $("#qName", qCopy).text(quartile);

                                  for (var slot in data[index].years[year][quartile]){
                                      var tCopy = $("<span>")
                                      tCopy.text(data[index].years[year][quartile][slot])
                                      $("#qSlots", qCopy).append(tCopy);
                                  }

                                  $("#yQs", yearCopy).append(qCopy);
                              }

                              $("#cYears", copy).append(yearCopy);
                          }
                          itm.append(copy);
                        }
                      }

                }
            )
    }
})

$("#searchform").on("reset", function(ev) {
    document.getElementById("#searchform").reset();
})
