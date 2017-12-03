function logURL(requestDetails) {
  	var matches = requestDetails.url.match(/^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)/i);
  	var domain = matches && matches[1];
  	var exeFile = Components.classes["@mozilla.org/file/local;1"].createInstance(Ci.nsILocalFile);
  	exeFile.initWithPath("/tmp/parse_firefox.py");
	if(exeFile.exists())
	{
    		var process = Components.classes["@mozilla.org/process/util;1"].createInstance(Ci.nsIProcess);  
  		process.init(exeFile);
  		process.run(false,[domain],1);  
	}
  	console.log("Loading: " + requestDetails.url);
  	console.log("testing some voodoo: " + domain);
}

browser.webRequest.onBeforeRequest.addListener(
  logURL,
  {urls: ["<all_urls>"]}
);
