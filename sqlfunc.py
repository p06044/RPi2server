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
    murl = 'https://jp.mercari.com/search?keyword='+decode+'&order=asc&sort=price&status=on_sale&page=1&status_on_sale=1&shipping_payer_id%5B2%5D=1&price_max=&price_min=&size_group=&brand_id=&brand_name=&category_root=&sort_order=price_asc&shipping_payer_id=2'
    yurl = 'https://auctions.yahoo.co.jp/search/search?p='+decode+'&ei=UTF-8&s1=cbids&o1=a'
    rurl = 'https://search.rakuten.co.jp/search/mall/'+decode+'/?f=2'
    furl = 'https://fril.jp/s?carriage=1&order=asc&query='+decode+'&sort=sell_price&transaction=selling'
#    mourl = 'https://www.mbok.jp/_l?o=1&q='+decode+'&c=80&sf=1'
    ydurl = 'https://www.yodobashi.com/?discontinued=false&sorttyp=SELL_PRICE_ASC&word='+decode

    aimgurl = 'https://66.media.tumblr.com/d0c8dee7bba07bb889cd3e934b3e3009/tumblr_pq9t9oGQGL1tdfmoeo1_250.png'
    mimgurl = 'https://www-mercari-jp.akamaized.net/assets/img/common/common/mercari_icon.png'
    yimgurl = 'https://66.media.tumblr.com/4487730ff053976c24df278eefdff802/tumblr_pq9timaxBo1tdfmoeo1_400.jpg'
    rimgurl = 'https://66.media.tumblr.com/e7e9a4d5a61ee8c4db9b846ae7bcc203/tumblr_pwz2bcMJ6t1v6viawo1_400.png'
    fimgurl = 'https://66.media.tumblr.com/ac635c15fa7a57836ca3de10291c0a9c/140655e2a483b24a-b3/s400x600/bee90275479a7667708eab95fda2f6d9d2119aaf.jpg'
    moimgurl = 'https://66.media.tumblr.com/fb02ddc8e3505dcaa06c212bcd5b7f81/3721f5ac44854105-e5/s250x400/b0686869cd0c21b8597300f6433903589e5c24f2.png'
    ydimgurl = 'https://64.media.tumblr.com/1253b4b164ce46f3117aa6c2067b63d1/dcdd2ada5249e8c1-e1/s540x810/15af1a28459f89d46539ef3e403d747eff74ecee.png'

    mlink = '<a href=\"'+murl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+mimgurl+' width="20" alt="TAG index" border="0"></a> '
    alink = '<a href=\"'+aurl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+aimgurl+' width="20" alt="TAG index" border="0"></a> '
    ylink = '<a href=\"'+yurl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+yimgurl+' width="20" alt="TAG index" border="0"></a> '
    rlink = '<a href=\"'+rurl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+rimgurl+' width="20" alt="TAG index" border="0"></a> '
    flink = '<a href=\"'+furl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+fimgurl+' width="20" alt="TAG index" border="0"></a> '
    ydlink = '<a href=\"'+ydurl+'\" class=\"btn-square-shadow\" target=\"_blank\"><img src='+ydimgurl+' width="20" alt="TAG index" border="0"></a> '
    button = name+'<button type=\"submit\" class=\"btn-square-shadow\" name=\"btn\" value=\"'+id+'\">del'+id+'</button><br/>'
    link = '<div>'+mlink+rlink+alink+ylink+flink+ydlink+button+'</div>'
#    return link
    return id, link

def link4for():
#   print "<form action=\"deletebutton.py\" method=\"get\" onSubmit=\"return check()\">"
    for i in range(0, recordcount()):
        print "<form action=\"deletebutton.py\" method=\"get\" onSubmit=\"return check("+link4(i)[0]+")\">"
        print link4(i)[1]
        print "</form>"
