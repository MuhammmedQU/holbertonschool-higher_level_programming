#!/usr/bin/python3
"""
'hbtn_0e_0_usa' bazasından adı 'N' ilə başlayan ştatları siyahılayan skript.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    # sys.argv[1] -> username, sys.argv[2] -> password, sys.argv[3] -> database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # SQL sorğusu: 'N' ilə başlayanları seçir və ID-yə görə sıralayır.
    # BINARY açar sözü böyük/kiçik hərf fərqini (N vs n) dəqiqləşdirir.
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Bütün uyğun sətirləri götürürük
    rows = cursor.fetchall()

    # Nəticələri çap edirik
    for row in rows:
        print(row)

    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()
