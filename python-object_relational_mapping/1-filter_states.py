#!/usr/bin/python3
"""Lists all states starting with N from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


def main():
    """Connects to MySQL database and prints states starting with N."""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
