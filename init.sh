#!/bin/bash
cd git
git init &
wait $!
git remote add origin https://github.com/p06044/RPi2server.git &
wait $!
git fetch &
wait $!
git merge origin/master &
wait $!
#login information
i=1
cat $HOME/login.txt | while read line
do
        if [ $i -eq 1 ]; then
                n=${line}
        elif [ $i -eq 2 ]; then
                m=${line}
        fi
        i=`expr $i + 1`
        if [ $i -eq 3 ]; then
		git config --global user.name $n
		git config --global user.email $m
        fi
done

mkdir /home/pi/gittxt
mv index.html /home/pi/gittxt/
#cp index.html /var/www/html/
#cp phpbutton.* /var/www/html/
#cp timer.html /var/www/html/
#cp tumblr.html /var/www/html/
crontab crontab.txt 
