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
    except IndexError:
        print(f"USAGE: {info[0]} <user> <password> <database>")
        exit(-1)
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM states WHERE name LIKE BINARY %(states)s",
                  {'states': info[4]})
    except IndexError:
        print("search string not passed")
        exit(-2)
    for row in c.fetchall():
        print(row)
    c.close()
    conn.close()
