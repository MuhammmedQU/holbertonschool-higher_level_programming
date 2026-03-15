#!/usr/bin/python3
"""List all cities of a state"""

import MySQLdb
import sys


def main():
    """Fetch cities by state name"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
    SELECT name
    FROM cities
    WHERE state_id = (
        SELECT id FROM states WHERE name = %s
    )
    ORDER BY id ASC
    """

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
