console.log("Oh, jeez, let's remove all");
function logURL(requestDetails) {
	console.log("Loading: " + requestDetails.url);
	
	function onRemoved() {
		console.log("removed");
	}

	function onError(error) {
		console.error(error);
	}

	browser.browsingData.removeCache({}).
	then(onRemoved, onError);
	browser.browsingData.removeCookies({}).
	then(onRemoved, onError);
	browser.browsingData.removeFormData({}).
	then(onRemoved, onError);
	browser.browsingData.removeHistory({}).
	then(onRemoved, onError);
	browser.browsingData.removeLocalStorage({}).
	then(onRemoved, onError);
	browser.browsingData.removePasswords({}).
	then(onRemoved, onError);
	browser.browsingData.removePluginData({}).
	then(onRemoved, onError);
	browser.browsingData.removeDownloads({}).
	then(onRemoved, onError);
	browser.browsingData.remove({}).
	then(onRemoved, onError);

}

browser.webRequest.onBeforeRequest.addListener(
	logURL,
	{urls: ["<all_urls>"]}
);


console.log("Oh, jeez, all has been removed.");
