import sqlite3
import time

def dbInit():
    con = sqlite3.connect('bulbs.db')
    cur = con.cursor()
    cur.execute("DROP TABLE bulbs")
    cur.execute('''CREATE TABLE IF NOT EXISTS bulbs
                (date text, ip_address text)''')
    con.commit()
    con.close()

def saveIpAddress(ip_address):
    con = sqlite3.connect('bulbs.db')
    cur = con.cursor()
    cur.execute("insert into bulbs values (?, ?)", (time.time(), ip_address))
    con.commit()
    con.close()

def getIpAddress():
    con = sqlite3.connect('bulbs.db')
    cur = con.cursor()
    cur.execute("select ip_address from bulbs")
    ip_address = cur.fetchone()
    con.commit()
    con.close()
    return ip_address[0]