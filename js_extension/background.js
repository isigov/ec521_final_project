console.log("Oh, jeez, let's remove all");

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

function logURL(requestDetails) {
    if (Math.random() < 0.9) {
        return;
    }
    function reqListener () {
        current_domain = getDomain(requestDetails.url);
        var patt = new RegExp(current_domain);
        console.log("Patt: " + patt);

        var url_list = this.responseText;
        console.log("url_list: " + url_list);

        var res = url_list.match(patt);
        console.log("res: " + res);

        console.log("Loading: " + requestDetails.url);

        function onRemoved() {
                console.log("removed");
        }

        function onError(error) {
                console.error(error);
        }

        if (res) {
            browser.browsingData.removeCache({}).
            then(onRemoved, onError);
            browser.browsingData.removeCookies({}).
            then(onRemoved, onError);
        }
    }
    var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", "http://128.197.127.31:1234/home/ec521/ec521_final_project/blacklist.txt");
    oReq.send();
}

browser.webRequest.onBeforeRequest.addListener(
	logURL,
	{urls: ["<all_urls>"]}
);


console.log("Oh, jeez, all has been removed.");
