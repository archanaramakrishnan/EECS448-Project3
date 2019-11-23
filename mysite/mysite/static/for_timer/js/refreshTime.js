
var start = document.getElementById("starttimer");
var dis = document.getElementById("countdown");
var previousTime;
//var timerLength = 30;
var timeoutID;
//dis.innerHTML = "Time Left: " + timerLength;

if(localStorage.getItem('myTime')){
    Update();
}

start.onclick = function () {
    localStorage.setItem('myTime', ((new Date()).getTime()));
    if (timeoutID != undefined) window.clearTimeout(timeoutID);
    setInterval(Update, 1000);
    Update();
}

function Update() {

    previousTime = localStorage.getItem('myTime');
    var timeStart = (new Date()- previousTime)/1000; //this will give
    dis.innerHTML =   timeStart + " seconds";
    timeoutID = window.setTimeout(Update, 100);
}
