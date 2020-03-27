#**Sumitha Ravindran **#
import pymysql
import sys
import time
import random
from datetime import datetime

REGION = 'us-east-2'
rds_host  = "databasebm.csmeylzksf11.us-east-2.rds.amazonaws.com"
name = "pi"
password = "project12"
db_name = "BabyTempDB"

conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

def saveData(email, temp, sts):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    global conn
    with conn.cursor() as cur:
        cur.execute("insert into babyTemp (email, temp, time, status) values( %s, %s, %s, %s)", (email, temp, now, sts))
        conn.commit()
        cur.close()
        print "Data saved to RDS..."

def getData(email):
    result = []
    global conn
    t = ""
    with conn.cursor() as cur:
        cur.execute("select * from babyTemp WHERE email=%s", email)
        conn.commit()
        cur.close()
        t += """\
<table style='border: 1px solid black'>
<tr>
    <th style='border: 1px solid black'>Date/Time</th>
    <th style='border: 1px solid black'>Temp</th>
    <th style='border: 1px solid black'>Status</th>
</tr>"""
        for row in cur:
            temp = (row)[2]
            time = (row)[3]
            status = (row)[4]
            t += "<tr><td style='border: 1px solid black'>" + str(time) + "</td><td style='border: 1px solid black'> temp was : "+ str(temp) +"</td><td style='border: 1px solid black'>" + str(status) + "</td></tr>"
        print ("Data from RDS...")
        t += "</table>"
        return t

def deleteData(email):
    result = []
    global conn
    with conn.cursor() as cur:
        cur.execute("delete from babyTemp WHERE email=%s", email)
        conn.commit()
        cur.close()
        print "Data Deleted to RDS..."
