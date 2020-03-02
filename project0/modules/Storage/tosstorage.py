import sqlite3
import subprocess
import os
def create_db():
    os.system("bash /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/scripts/jah-db.sh")
    #subprocess.call(['bash', 'projects/cs5293-project0/scripts/jad-db.sh'])
def kill_db():
    os.system("bash /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/scripts/clean-db.sh")
    #subprocess.call(['bash', 'projects/cs5293-project0/scripts/clean-db.sh'])
def connect_to_db():
    return sqlite3.connect('normanpd.db')

def insert_into_crime_report(summary: tuple):
    """

    :param summary:
    :return:
    """
    connection = connect_to_db()
    usr = connection.cursor()

    usr.execute("INSERT INTO CrimeReport VALUES (?,?,?,?,?,?,?,?,?,?,?)", summary)

    connection.commit()

    connection.close() ## close connection

def insert_into_incident_report(summary: tuple):
    """

    :param summary:
    :return:
    """
    connection = connect_to_db()
    usr = connection.cursor()

    usr.execute("INSERT INTO Incident VALUES (?,?,?,?)", summary)

    connection.commit()

    connection.close() ## close connection

def fetch_CrimeReport_table():
    """

    :return:
    """
    connection = connect_to_db()
    usr = connection.cursor()
    usr.execute("SELECT * from Incident")
    storage = usr.fetchall()
    connection.close()
    return storage

def fetch_CrimeReport_table():
    """

    :return:
    """
    connection = connect_to_db()
    usr = connection.cursor()
    usr.execute("SELECT * from CrimeReport")
    storage = usr.fetchall()
    connection.close()
    return storage

def fetch_CrimeReport_value(field: str, val: str):
    """

    :param field:
    :param val:
    :return:
    """
    connection = connect_to_db()
    usr = connection.cursor()
    usr.execute("SELECT offense FROM CrimeReport WHERE ?=?", (field, val))
    storage = usr.fetchall()
    print(storage)
    connection.close()
    return storage

if __name__ == "__main__":
    pass
    #print(f"tosstorage.py is designed to handle database reading, manipulation, and transformation")
    #insert_into_crime_report()

    #read_from_crime_report()
    #kill_db()
    #create_db()