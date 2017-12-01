
NeverCookie
-----------

Extension for removing evercookie



TODO List
---------

1. Check (in VM) which version of firefox removes evercookies
2. Decide on extension type (legacy vs. webex), depending on firefox version
3. Implement extension that checks if domain name is in the blacklist and deletes evercookie
4. Build server to receive `eval` requests and crawl them
5. In extension, send requests for `eval` to the blacklist to server
6. Build server to send a compressed blacklist upon `update` request
7. In extension, update the list, remove old cookies
8. Implement BASIC authentication for evercookie
9. Implement BASIC authentication for crawler
10. Prepare slideshow
11. Prepare video
11. Write report
