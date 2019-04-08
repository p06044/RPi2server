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
    sql = "SELECT COUNT(*) FROM line;"
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
    sql = "select * from line order by id desc limit 1 offset "+str(int(num))+";"
    cur.execute(sql)
    rows = cur.fetchall()
    id = rows[0][0]
    name = rows[0][1]
    cur.close()
    conn.close()
    return id, name

def selectbyid(num):
    conn = MySQLdb.connect(
        user = 'pi',
        host = 'localhost',
        passwd = 'raspberry',
        db = 'memopad',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "SELECT * FROM line WHERE id = "+num+";"
    cur.execute(sql)
    rows = cur.fetchall()
    id = rows[0][0]
    name = rows[0][1]
    cur.close()
    conn.close()
    return id, name

def additem(name):
    conn = MySQLdb.connect(
        user = 'pi',
        host = 'localhost',
        passwd = 'raspberry',
        db = 'memopad',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "INSERT INTO line(name) VALUES('"+name+"');"
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
    sql = "DELETE FROM line WHERE id = "+id+";"
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

def link4(num):
    id = str(selectbycount(num)[0])
    name = selectbycount(num)[1].encode('utf-8')
    button = name+'<button type=\"submit\" class=\"btn-square-shadow\" name=\"btn\" value=\"'+id+'\">del'+id+'</button><br/>'
    link = '<div>'+button+'</div>'
    return link

def link4for():
    print "<form action=\"memodelbutton.py\" method=\"get\">"
    for i in range(0, recordcount()):
        print link4(i)
    print "</form>"
