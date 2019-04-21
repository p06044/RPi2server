#!/usr/bin/python
#coding:utf-8
import datetime
import cgifunc
import flashsqlfunc

cgifunc.head('flash')
cgifunc.link('flash')
date = datetime.date.today()
print date 
cgifunc.afi()
print "<br/>"
#print "<div><input type=\"button\" class=\"btn-square-shadow\" value=\"英単語\" onclick=\"clickBtn()\"/><span id=\"p2\">日本語訳</span></div>"
#print "<script>"
#print "document.getElementById(\'p2\').style.visibility =\"hidden\";"
#print "function clickBtn(){"
#print "    const p2 = document.getElementById(\'p2\');"
#print "    if(p2.style.visibility==\'visible\'){"
#print "        p2.style.visibility =\'hidden\';"
#print "    }else{"
#print "        p2.style.visibility =\'visible\';"
#print "    }"
#print "}"
#print "</script>"

print "<form method=\"POST\" action=\"flashadditem.py\">"
print "<p>単語<input type=\"text\" name=\"word\" id=\"addtext\">訳<input type=\"text\" name=\"translate\" id=\"addtext\"><input type=\"submit\" class=\"btn-square-shadow\" value=\"追加\"></p>"
print "<script type=\"text/javascript\">document.getElementById('addtext').focus();</script>"
print "</form>"

flashsqlfunc.link4for()
cgifunc.end()
