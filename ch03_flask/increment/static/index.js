var n=0;
var num = document.querySelector("#num");
var increase = document.querySelector("#increase");
var submit = document.querySelector("#submit");

increase.addEventListener("click", function() {
    n = n+1;
    num.innerHTML = n;
})

submit.addEventListener("click", function() {
    location.href='http://10.150.2.52:5001/'+n
    n = 0;
    num.innerHTML = n;
})
