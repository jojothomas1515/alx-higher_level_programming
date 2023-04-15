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
    try:
        c.execute("SELECT c.name FROM cities c " +
                  "INNER JOIN states st WHERE st.id = state_id "+
                  "AND st.name LIKE BINARY %(state)s "+
                  "ORDER BY c.id",
                  {'state': info[4]})
    except IndexError as e:
        print('please pass the state')

    li = []
    for row in c.fetchall():
        li.append(row[0])
    if (len(li) != 0):
        print(" ".join(li))
    c.close()
    conn.close()
