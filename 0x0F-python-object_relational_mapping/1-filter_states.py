#!/usr/bin/python3

"""
show all states
"""
import MySQLdb
import sys

if __name__ == '__main__':
    info = sys.argv
    try:
        conn = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=str(info[1]),
                               password=str(info[2]),
                               database=str(info[3]),
                               charset="utf8")
    except IndexError as e:
        print(f"USAGE: {info[0]} <user> <password> <database>")
        exit(-1)
    c = conn.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    for row in c.fetchall():
        print(row)

    c.close()
    conn.close()
