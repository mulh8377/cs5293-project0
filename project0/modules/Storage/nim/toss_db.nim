import db_sqlite

let db = open("normanpd.db", "", "", "")

db.exec(sql"DROP TABLE IF EXISTS OFFICER")
echo "table officer is gone"
db.exec(sql"DROP TABLE IF EXISTS CRIMINAL")
echo "table criminal is gone"
db.exec(sql"DROP TABLE IF EXISTS Incident")
echo "table Incident is gone"
db.exec(sql"DROP TABLE IF EXISTS CrimeReport")
echo "table crimereport is gone"

db.close()
echo "database is closed"
