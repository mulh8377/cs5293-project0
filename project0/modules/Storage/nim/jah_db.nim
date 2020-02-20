import db_sqlite

let db = open("normanpd.db", "", "", "")


db.exec(sql"""CREATE TABLE CrimeReport (
    arresttime TEXT,
    casenumber TEXT,
    arrest_location TEXT,
    offense TEXT,
    arresteename TEXT,
    arresteebirthday TEXT,
    city TEXT,
    state TEXT,
    zip TEXT,
    status TEXT,
    officer TEXT)""")

db.exec(sql"""CREATE TABLE Scene (
    caseno TEXT,
    dateno TEXT,
    locationat TEXT,
    zipcode TEXT,
    citylabel TEXT
)""")

db.exec(sql"""create table Officer ( 
    caseno TEXT,
    dateno TEXT,
    namelabel TEXT,
    locationlabel TEXT,
    chargelabel TEXT
 )""")

db.exec(sql"""create table Criminal ( 
    caseno TEXT,
    dateofarrest TEXT,
    nameofarrest TEXT,
    dateofbirth TEXT,
    charge TEXT
 )""")

db.close()

