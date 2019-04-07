#!/usr/bin/python
#coding: utf-8
import MySQLdb

def recordcount():
    conn = MySQLdb.connect(
        user = 'pi',
        host = 'localhost',
        passwd = 'raspberry',
        db = 'auction',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "SELECT COUNT(*) FROM item;"
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
        db = 'auction',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "select * from auction.item order by id limit 1 offset "+str(int(num))+";"
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
        db = 'auction',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "SELECT * FROM item WHERE id = "+num+";"
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
        db = 'auction',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "INSERT INTO item(name) VALUES('"+name+"');"
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

def delete(id):
    conn = MySQLdb.connect(
        user = 'pi',
        host = 'localhost',
        passwd = 'raspberry',
        db = 'auction',
        charset = 'utf8'
        )
    cur = conn.cursor()
    sql = "DELETE FROM auction.item WHERE id = "+id+";"
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
