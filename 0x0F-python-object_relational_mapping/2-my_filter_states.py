#!/usr/bin/python3
"""
Script that filters by state name from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{}' ORDER BY id ASC;"
                .format(state))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
