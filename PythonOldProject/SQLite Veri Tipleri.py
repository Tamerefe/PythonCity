# YAPISI VE OLUSTURMA

import sqlite3

db = sqlite3.connect("veritabani.db")

#
# veriler = [
# (12,45,89),
# (45,68,72),
# (65,23,74),
# (15,61,75)
# ]
imlec = db.cursor()

imle.execute("SELECT * FROM 'oyuncular'")

print(imlec.fetchone())

print(imlec.fetchmany(3))


# veriler = imlec.fetchall()

# for ver in veriler:
#     print(ver)

# imlec.execute("CREATE TABLE IF NOT EXISTS 'hayat' (yas,kilo,boy)")
# for veri in veriler :
#     imlec.execute("INSERT INTO  'oyuncular' VALUES (?,?,?)",veri)

# imlec.execute("INSERT INTO  'oyuncular' VALUES ('32','89','195')")

# db.commit()

db.close()
