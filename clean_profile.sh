#!/bin/bash
# cd /home/ec521/ec521_final_project/cleanProfile
# rm -rf !(times.json)

find /home/ec521/ec521_final_project/cleanProfile -type f -not -name 'times.json' -print0 | xargs -0 rm --