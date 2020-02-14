import db_sqlite
let db = open("normanpd.db", "", "", "")
echo "1,2,3,4,5,6,7,8,9,10"
for k in db.fastRows(sql"SELECT * from CrimeReport"):
    echo k
db.close()