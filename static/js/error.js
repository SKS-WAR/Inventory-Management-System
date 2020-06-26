var up = true;
var value = 0;
var increment = 1;
var ceiling = 404;

function PerformCalc() {
  if (up == true && value <= ceiling) {
    value += increment

    if (value == ceiling) {
      up = false;
    }
  }

  document.getElementById('counter').innerHTML = 'Error: ' + value + '<br />';
}
setInterval(PerformCalc, 10);