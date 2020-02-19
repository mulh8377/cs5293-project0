import sqlite3
import os
import modules.Crime.crime as crime

def create_db():
    os.system("bash /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/scripts/jah-db.sh")
def kill_db():
    os.system("bash /home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/scripts/clean-db.sh")
def connect_to_db():
    return sqlite3.connect('../../../normanpd.db')

def insert_into_crime_report(summary: crime.CrimeReport):
    connection = connect_to_db()
    usr = connection.cursor()

    connection.commit()

    connection.close() ## close connection

def read_from_crime_report():
    connection = connect_to_db()
    usr = connection.cursor()
    if connection:
        print(connection)
    connection.close()

if __name__ == "__main__":
    #print(f"tosstorage.py is designed to handle database reading, manipulation, and transformation")
    #insert_into_crime_report()

    #read_from_crime_report()
    #kill_db()
    create_db()