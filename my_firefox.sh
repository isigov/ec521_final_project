#!/bin/bash

firefox=$(which firefox)
cleaner="python ./parse_firefox.py"
website_list="./js_extension/website_list.txt"

$firefox &
wait $!

cat $website_list | xargs -L 1 $cleaner
