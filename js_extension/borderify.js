console.log("Oh, jeez, I debugged");

document.body.style.border = "5px solid red";

// current url
console.log(window.content.location.href);

// string match
var str = "The best things in life are free";
var patt = new RegExp("e");
var res = patt.test(str);

// GET request
var my_url = "http://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b1b15e88fa797225412429c1c50c122a1";
var my_img = "http://www.bu.edu/homepage/feature-images/sub/hoopheal.jpg"


$(document).ready(function(){
	
	function reqListener () {
  		console.log(this.responseText);
	}

	var oReq = new XMLHttpRequest();
	oReq.addEventListener("load", reqListener);
	//oReq.open("GET", "https://www.mozilla.org");
	oReq.open("GET", "https://www.google.com");
	oReq.send();
	console.log('end');
	
	$.get('test.txt', function(data) {
		console.log(data)
	}, 'text');
	
});

console.log("Oh, jeez, I debugged in the end");





