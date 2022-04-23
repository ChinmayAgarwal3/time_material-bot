#!/bin/bash
# rename and move video to goodle drive sync folder
cd Documents/projects/birthday_bot
python3 bot.py 
WAIT=$!
wait $WAIT

counter=1
while [ $counter -le 10 ]
do
    echo $counter
    mv ccv_00000.mp4 $counter
    gio move $counter google-drive://kanika.s2019bos@srisriuniversity.edu.in/
    ((counter++))
done


