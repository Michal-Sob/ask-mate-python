function showPassword() {

    let x = document.getElementById("password");
    let span = document.getElementById("checkbox_text");


    if (span.innerHTML === "Hide") {
        span.innerHTML = "Show"
    }
    else {
        span.innerHTML = "Hide"
    }


    if (x.type === "password") {
    x.type = "text";
    }
    else {
    x.type = "password";
    }
}


function thumbToggle(x) {
  x.classList.toggle("fa-thumbs-down");
}