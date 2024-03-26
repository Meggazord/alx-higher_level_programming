#!/usr/bin/python3
"""
Script that filters by state name safely from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

def search_state(username, password, database, state_name):
    conn = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306)
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    username, password, database, state_name = sys.argv[1:]
    if ';' in state_name:
        print("Error: Invalid input.")
        sys.exit(1)
    else:   
        search_state(username, password, database, state_name)
