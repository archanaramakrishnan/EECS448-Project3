
var start = document.getElementById("starttimer");
var display = document.getElementById("countdown");
var reminder = document.getElementById("reminders");
var previousTime;
//var timerLength = 30;
var timeoutID;
//dis.innerHTML = "Time Left: " + timerLength;

if(localStorage.getItem('myTime')){
    Update();
}

start.onclick = function () {
    localStorage.setItem('myTime', ((new Date()).getTime()));
    //setInterval(Update, 1000);
    Update();
    //mytime = setTimeout(remind(10),10000);
}

function Update() {
    previousTime = localStorage.getItem('myTime');
    var timeStart = (new Date()- previousTime)/1000;
    if (parseInt(timeStart) >= 30) {
      reminder.innerHTML = "It has been 30 seconds";
   }
    var hours = parseInt(timeStart / 3600 );
    var minutes = parseInt((timeStart - (hours * 3600)) / 60 );
    var seconds = Math.floor((timeStart - ((hours * 3600) + (minutes * 60))));
    var finalResult = (hours < 10 ? "0" + hours : hours) + ":" + (minutes < 10 ? "0" + minutes : minutes) + ":" + (seconds  < 10 ? "0" + seconds : seconds);
    display.innerHTML = finalResult;
    setInterval(Update, 1000);

  //  setTimeout(remind(10), 10000);
}

//function remind(msg1) {
  //  var msg = "This is a reminder after " + msg1 +" Secs";
  //  reminder.innerHTML = msg;
//}
