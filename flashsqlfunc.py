#!/usr/bin/python
#coding: utf-8
import MySQLdb
import urllib

def recordcount():
    conn = MySQLdb.connect(
        user = 'pi',
        host = 'localhost',
        passwd = 'raspberry',
        db = 'memopad',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "SELECT COUNT(*) FROM flashcard;"
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows[0][0]

def selectbycount(num):
    conn = MySQLdb.connect(
        user = 'pi',
        host = 'localhost',
        passwd = 'raspberry',
        db = 'memopad',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "select * from flashcard order by id desc limit 1 offset "+str(int(num))+";"
    cur.execute(sql)
    rows = cur.fetchall()
    id = rows[0][0]
    word = rows[0][2]
    translate = rows[0][3]
    cur.close()
    conn.close()
    return id, word, translate

def selectbyid(num):
    conn = MySQLdb.connect(
        user = 'pi',
        host = 'localhost',
        passwd = 'raspberry',
        db = 'memopad',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "SELECT * FROM flashcard WHERE id = "+num+";"
    cur.execute(sql)
    rows = cur.fetchall()
    id = rows[0][0]
    word = rows[0][2]
    cur.close()
    conn.close()
    return id, word

def additem(word, translate):
    conn = MySQLdb.connect(
        user = 'pi',
        host = 'localhost',
        passwd = 'raspberry',
        db = 'memopad',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "INSERT INTO flashcard(word, translate) VALUES('"+word+"', '"+translate+"');"
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

def delete(id):
    conn = MySQLdb.connect(
        user = 'pi',
        host = 'localhost',
        passwd = 'raspberry',
        db = 'memopad',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "DELETE FROM flashcard WHERE id = "+id+";"
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

def link4(num):
    id = str(selectbycount(num)[0])
    word = selectbycount(num)[1].encode('utf-8')
    translate = selectbycount(num)[2].encode('utf-8')
    js = "<script> document.getElementById(\'p"+id+"\').style.visibility =\"hidden\"; function clickBtn"+id+"(){const p"+id+" = document.getElementById(\'p"+id+"\'); if(p"+id+".style.visibility==\'visible\'){p"+id+".style.visibility =\'hidden\';}else{p"+id+".style.visibility =\'visible\';}}</script>"
    button = '<input type=\"button\" class=\"btn-square-shadow\" value=\"'+word+'\" onclick=\"clickBtn'+id+'()\"/><span id=\"p'+id+'\">'+translate+'</span><button type=\"submit\" class=\"btn-square-shadow\" name=\"btn\" value=\"'+id+'\">del'+id+'</button><br/>'
    link = '<div>'+button+'</div>'+js
    return link

def link4for():
    print "<form action=\"flashdelbutton.py\" method=\"get\" onSubmit=\"return check()\">"
    for i in range(0, recordcount()):
        print link4(i)
    print "</form>"
