function hide_qs() {
    document.getElementById("question_response").style.display = "none";
}

function show_qs() {
    document.getElementById("question_response").style.display = "block";

    setTimeout(function(){document.getElementById("question_response").style.display = "none"},5000)
}

hide_qs();