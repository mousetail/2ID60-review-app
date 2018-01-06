$("#searchform").on("submit", function(ev) {
    ev.preventDefault();
    var value = $("#idfield").val();
    console.log(value);
    if (value.length > 4){
        window.location = "/course/"+value;
    }
})