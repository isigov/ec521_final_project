#!/bin/bash

firefox=$(which firefox)
cleaner="python ./parse_firefox.py"
website_list=$(find "$HOME/.mozilla/firefox/dtlcd1sy.default/browser-extension-data/" -name '*.js')

$firefox &
wait $!

cat $website_list | xargs -L 1 $cleaner
# rm -r "$HOME/.mozilla/firefox/dtlcd1sy.default/browser-extension-data"
