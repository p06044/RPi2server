#!/bin/sh
html=`curl "http://www.toeic.or.jp/toeic/pr.html?utm_source=iibc&utm_medium=mail&utm_term=&utm_content=&utm_campaign=iibc_mail_exercise_lp_2016"`
content=`echo -e "${html}" | grep -e \<p\> -e \<h3\> | sed -e 's/<p>//g' -e 's/<\/p>//g' -e 's/<h3>//g' -e 's/<\/h3>//g' -e '/<noscript>/d' -e '/<\/br/d' -e '/<font/d' -e '/<strong>/d' -e '/日常/d'`
title=`echo "${content}" | sed -n '1p'`
/usr/local/bin/wp post create --post_title="${title}" --post_content="${content}" --post_status=publish --porcelain --path=/var/www

#一時的にhtmlに落とす
html=`date +"%Y%m%d"`.html
#wget -O /home/pi/${html} http://www.toeic.or.jp/toeic/pr.html?utm_source=iibc&utm_medium=mail&utm_term=&utm_content=&utm_campaign=iibc_mail_exercise_lp_2016
wget -O /home/pi/${html} "https://www.iibc-global.org/toeic/test/lr/about/pr.html?utm_source=iibc&utm_medium=mail&utm_campaign=iibc_mail_exercise_over23
"
sleep 2s
mv /home/pi/${html} /var/www

