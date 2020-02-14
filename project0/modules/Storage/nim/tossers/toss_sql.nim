import db_sqlite
let db = open("../../../normanpd.db", "", "", "")
for j in db.fastRows(sql"SELECT * from OFFICER"):
    echo j
for k in db.fastRows(sql"SELECT * from CRIMINAL"):
    echo k
for i in db.fastRows(sql"SELECT * from SCENE"):
    echo i
echo "closing the database"
db.close()