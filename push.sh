#!/bin/bash
i=1
cat $HOME/gitpass.txt | while read line
do
        if [ $i -eq 1 ]; then
                n=${line}
        elif [ $i -eq 2 ]; then
                m=${line}
	        fi
        i=`expr $i + 1`
	if [ $i -eq 3 ]; then
		expect -c "
		spawn git push origin master
		expect \"Username for 'https://github.com':\"
		send -- \"${n}\n\"
		expect \"Password for 'https://p06044@github.com':\"
		send -- \"${m}\n\"
		"
	fi
done
