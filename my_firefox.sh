#!/bin/bash

firefox=$(which firefox)

$firefox &
wait $!

cleaner="python ./parse_firefox.py"
website_list=$(find "$HOME/.mozilla/firefox/dtlcd1sy.default/browser-extension-data/" -name '*.js')

$cleaner "$(cat $website_list)"
rm -r "$HOME/.mozilla/firefox/dtlcd1sy.default/browser-extension-data"
