import db_sqlite
let db = open("normanpd.db", "", "", "")
echo "1,2,3,4,5"
for k in db.fastRows(sql"SELECT * from SCENE"):
    echo k
db.close()