console.log("Oh, jeez, let's remove all");

// var {Cc, Ci} = require("chrome");
//         var window = Cc["@mozilla.org/appshell/window-mediator;1"]
//             .getService(Ci.nsIWindowMediator)
//             .getMostRecentWindow("navigator:browser");
//         var notifyBox = window.gBrowser.getNotificationBox();
//         notifyBox.appendNotification(
//                 'evercookie seen', 'evercookie',
//                 'chrome://browser/skin/Info.png',
//                 notifyBox.PRIORITY_INFO_HIGH, 0, 0);

// function getWindowFromRequest(requestDetails) {
//     function displayWarning(curWindow) {
//         curWindow.getNotificationBox(curWindow);
//     }
//     function getWindow(tabObject) {
//         var getting = browser.windows.get(tabObject.windowId);
//         getting.then(displayWarning);
//     }
//     var getTab = browser.tabs.get(requestDetails.tabId);
//     getTab.then(getWindow);
// }

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
	// browser.browsingData.removeFormData({}).
	// then(onRemoved, onError);
	// browser.browsingData.removeHistory({}).
	// then(onRemoved, onError);
	browser.browsingData.removeLocalStorage({}).
	then(onRemoved, onError);
	// browser.browsingData.removePasswords({}).
	// then(onRemoved, onError);
	// browser.browsingData.removePluginData({}).
	// then(onRemoved, onError);
	// browser.browsingData.removeDownloads({}).
	// then(onRemoved, onError);
	// browser.browsingData.remove({}).
	// then(onRemoved, onError);
        // try {
         // } catch (e) {}
    };

}

browser.webRequest.onBeforeRequest.addListener(
	logURL,
	{urls: ["<all_urls>"]}
);


console.log("Oh, jeez, all has been removed.");
