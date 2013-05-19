"""
    the nation of the ip
    the database from www.ip2nation.com
"""
import sqlite3
import os
import socket
import struct
import threading
import sys
import time

def loading(target, args):
    interval = 0.1
    t = threading.Thread(target=target, args=args)
    t.start()
    while True:
        sys.stdout.write('\b-')
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write('\b\\')
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write('\b|')
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write('\b/')
        sys.stdout.flush()
        if t.isAlive():
            t.join(interval)
        else:
            break;
    sys.stdout.flush('\b')
    return 
def createDB(file):
    db = sqlite3.connect(file)
    with open('ip2nation.sql', 'r') as sqlfile:
        create_sql = sqlfile.read()
        create_sql = create_sql.replace('unsigned', 'primary key')
        create_sql = create_sql.replace(',\n  KEY ip (ip)', '')
        create_sql = create_sql.replace(',  \n  PRIMARY KEY  (code),\n  KEY code (code)','')
        create_sql = create_sql.replace(
        "code varchar(4) NOT NULL default ''", 
        "code varchar(4) primary key NOT NULL default ''")
        db.executescript(create_sql)
        sqlfile.close()
    db.close()

def nation(ip):
    file = 'ip2nation.db'
    db = sqlite3.connect(file)
    if 0 == os.path.getsize(file):
        loading(createDB,(file,))

    sql = ("""\
SELECT
    c.country
FROM
    ip2nationCountries c, 
    ip2nation i
WHERE
    i.ip < %s
    AND
    c.code = i.country
ORDER BY
    i.ip DESC
LIMIT 0,1""" % struct.unpack("!l", socket.inet_aton(ip)))
    c = db.cursor()
    c.execute(sql)
    result = c.fetchall()
    c.close()
    db.close()
    return result

