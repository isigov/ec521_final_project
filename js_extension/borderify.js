console.log("Oh, jeez, I debugged");

document.body.style.border = "5px solid red";

// current url
// console.log(window.content.location.href);
function getDomain(url, subdomain) {
    subdomain = subdomain || false;

    url = url.replace(/(https?:\/\/)?(www.)?/i, '');

    if (!subdomain) {
        url = url.split('.');

        url = url.slice(url.length - 2).join('.');
    }

    if (url.indexOf('/') !== -1) {
        return url.split('/')[0];
    }

    return url;
}

console.log(getDomain(window.content.location.href));

// string match
var str = "The best things in life are free";
var patt = new RegExp("e");
var res = patt.test(str);

// GET request
var my_url = "http://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b1b15e88fa797225412429c1c50c122a1";
var my_img = "http://www.bu.edu/homepage/feature-images/sub/hoopheal.jpg"


$(document).ready(function(){

	var total_list = ""
	
	function reqListener () {
		
		current_domain = getDomain(window.content.location.href)
		var patt = new RegExp(current_domain);
		console.log("Patt: " + patt);

		var url_list = this.responseText;
		console.log("url_list: " + url_list);

		var res = url_list.match(patt);
		console.log("res: " + res);

		if (res) {
			console.log("We have the url");
		} else {

			console.log("We do not have the url");

			function postListener () {
				console.log("POST: " + this.responseText);
			}

			var postReq = new XMLHttpRequest();
			postReq.addEventListener("load", postListener);
			//oReq.open("GET", "https://www.mozilla.org");
			postReq.open("POST", "http://128.197.127.31:1234");
			postReq.send("eval&" + current_domain);


		}
	}

	var oReq = new XMLHttpRequest();
	oReq.addEventListener("load", reqListener);
	//oReq.open("GET", "https://www.mozilla.org");
	oReq.open("GET", "http://128.197.127.31:1234/home/ec521/ec521_final_project/blacklist.txt");
	oReq.send();

	console.log('end');

	
});

var reader = new FileReader();

reader.onload = function(e) {
	var text = reader.result;
	console.log(text);
}

reader.readAsData('test.txt');

console.log("Oh, jeez, I debugged in the end");





