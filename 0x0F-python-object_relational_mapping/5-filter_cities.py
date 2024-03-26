#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

def filter_cities_by_state(username, password, database, state_name):
    try:
        conn = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        cur = conn.cursor()
        query = """
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """
        cur.execute(query, (state_name,))
        rows = cur.fetchall()
        if rows:
            cities = ', '.join(row[0] for row in rows)
            print(cities)
        else:
            print("No cities found for the state:", state_name)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    username, password, database, state_name = sys.argv[1:]
    filter_cities_by_state(username, password, database, state_name)
