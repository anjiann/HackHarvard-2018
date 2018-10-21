
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;

var slider2 = document.getElementById("myRange2");
var output2 = document.getElementById("demo2");
output2.innerHTML = slider.value;

var rgbValue = {r: 125, g: 125, b: 125}; 

slider.oninput = function() {
     output.innerHTML = slider.value;
     if(slider.value < 50) {
      rgbValue.r += 5;
      rgbValue.g += 5;
      // rgbValue.b+=5;
     }
     else {
      rgbValue.r+=5;
      // rgbValue.g-=5;
      rgbValue.b+=5;
     }
     document.body.style.backgroundColor = "rgb(" + rgbValue.r + ", " + rgbValue.g + ", " + rgbValue.b + ")";
 }

slider2.oninput = function() {
     output2.innerHTML = slider2.value;
 }

