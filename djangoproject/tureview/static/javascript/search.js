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
                   "slot": $("#timeslotfield").val(),
                   "quartile": $("#quartilefield").val()
                   }
            }).done(
                function(data) {
                    var itm = $("#result");
                    itm.empty();
                    for (var index in data){
                        var copy = $("#courseTemplate").clone();
                        $(copy).css("display", "")
                        $(copy).attr("id", "cTemplate"+index)
                        $("#cID", copy).text(data[index].id);
                        $("#cName", copy).text(data[index].name);
                        $("#cShortDesc", copy).text(data[index].shortDesc);
                        $("#cLongDesc", copy).text(data[index].longDesc);

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
            )
    }
})