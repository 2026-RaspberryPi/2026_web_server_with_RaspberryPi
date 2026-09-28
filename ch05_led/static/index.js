var led = document.querySelector("#led");
var on = document.querySelector("#on");
var off = document.querySelector("#off");

on.addEventListener("click", function() {
    fetch('/on', {
        method: 'GET'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        return response.text(); // JSON이면 response.json() 사용
    })
    .then(result => {
        led.src = "static/on.png";
    })
    .catch(error => {
        alert(error);
    });
});


off.addEventListener("click", function() {
    fetch('/off', {
        method: 'GET'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        return response.text(); // JSON이면 response.json() 사용
    })
    .then(result => {
        led.src = "static/off.png";
    })
    .catch(error => {
        alert(error);
    });
});
