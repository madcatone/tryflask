#-*- coding:utf-8 -*-
__author__ = 'apple'
import psycopg2

def select():
    conn_string = "host='localhost' dbname='dbname' user='postgres' password='password'"
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("select * from \"problem_mail\" order by p_date desc limit 100;")
    records = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return records

if __name__ == '__main__':
    select()
