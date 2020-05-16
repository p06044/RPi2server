#!/usr/bin/python
#coding: utf-8
import MySQLdb
import urllib

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
    sql = "select * from auction.item order by id desc limit 1 offset "+str(int(num))+";"
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

def link4(num):
    id = str(selectbycount(num)[0])
    name = selectbycount(num)[1].encode('utf-8')
    decode = urllib.quote(name)
    aurl = 'https://www.amazon.co.jp/s?k='+decode+'&s=price-asc-rank&qid=1555949145&ref=sr_st_price-asc-rank'
    murl = 'https://www.mercari.com/jp/search/?sort_order=price_asc&keyword='+decode+'&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max=&shipping_payer_id%5B2%5D=1&status_on_sale=1'
    yurl = 'https://auctions.yahoo.co.jp/search/search?p='+decode+'&ei=UTF-8&s1=cbids&o1=a'
    rurl = 'https://search.rakuten.co.jp/search/mall/'+decode+'/'
#    rurl = 'https://fril.jp/search/'+decode+'?order=asc&sort=sell_price&transaction=selling'
    furl = 'https://fril.jp/s?query='+decode+'&carriage=1&transaction=selling'
    aimgurl = 'https://66.media.tumblr.com/d0c8dee7bba07bb889cd3e934b3e3009/tumblr_pq9t9oGQGL1tdfmoeo1_250.png'
    mimgurl = 'https://www-mercari-jp.akamaized.net/assets/img/common/common/mercari_icon.png'
    yimgurl = 'https://66.media.tumblr.com/4487730ff053976c24df278eefdff802/tumblr_pq9timaxBo1tdfmoeo1_400.jpg'
    rimgurl = 'https://66.media.tumblr.com/e7e9a4d5a61ee8c4db9b846ae7bcc203/tumblr_pwz2bcMJ6t1v6viawo1_400.png'
    fimgurl = 'https://66.media.tumblr.com/ac635c15fa7a57836ca3de10291c0a9c/140655e2a483b24a-b3/s400x600/bee90275479a7667708eab95fda2f6d9d2119aaf.jpg'
    mlink = '<a href=\"'+murl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+mimgurl+' width="20" alt="TAG index" border="0"></a> '
    alink = '<a href=\"'+aurl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+aimgurl+' width="20" alt="TAG index" border="0"></a> '
    ylink = '<a href=\"'+yurl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+yimgurl+' width="20" alt="TAG index" border="0"></a> '
    rlink = '<a href=\"'+rurl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+rimgurl+' width="20" alt="TAG index" border="0"></a> '
    flink = '<a href=\"'+furl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+fimgurl+' width="20" alt="TAG index" border="0"></a> '
#    rlink = '<a href=\"'+rurl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src="https://asset.fril.jp/assets/new_web/icon_fril-97af0f192f84d4c9b11a13e51473f60125be6cd4be3e611fb074eb876ffe36a0.png" width="20" alt="TAG index" border="0"></a> '
    button = name+'<button type=\"submit\" class=\"btn-square-shadow\" name=\"btn\" value=\"'+id+'\">del'+id+'</button><br/>'
    link = '<div>'+mlink+rlink+alink+ylink+flink+button+'</div>'
    return link

def link4for():
    print "<form action=\"deletebutton.py\" method=\"get\" onSubmit=\"return check()\">"
    for i in range(0, recordcount()):
        print link4(i)
    print "</form>"
