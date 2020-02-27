import argparse
import tempfile
import sys
import os
import PyPDF2
import time
import subprocess
import pandas as pd
import modules.Crime.crime as Crime
import modules.Editor.tosspdf as T_PDF
import modules.Storage.tosstorage as T_Storage
import modules.Utility.utility as T_Utility

def fetchincidents(url, tipe):
    if url == "all":                            # default parameter if make run-project is called.
        data_loc = T_Utility.fetch_txt_all()
    else:
        data_loc = T_Utility.fetch_results(url) # alternative if user runs pipenv run python project0/main.py --arrests <url>
    extractincidents(data=data_loc, tipe=tipe)

def extractincidents(data, tipe):
    #print("extract the pdf fields here")
    """
    TODO:
    """
    subprocess.call(['bash', './scripts/transform-pdf.sh'])
    os.system('clear')
    time.sleep(0.3)
    #subprocess.call(['cat', './data/txt/arrest/ArrestSummary.txt'])
    #results = T_Utility.extract_results(data)
    if tipe == 1:
        data = pd.read_csv('./data/csv/arrest/arrest.csv')
    #print(data)
    elif tipe == 2:
        data = pd.read_csv('data/csv/incident/incident.csv')
    #data.to_sql('CrimeReport', T_Storage.connect_to_db(), if_exists='append', index=False)
    else:
        print('error')
    importincidents(data, tipe)
def importincidents(data, tipe):
    #print(data)
    #connection = T_Storage.connect_to_db()
    #print(connection)
    if tipe == 1:
        summary_tuples = list(data.itertuples(index=False, name=None))
        #print(summary_tuples)
        for row, summary in enumerate(summary_tuples):
            T_Storage.insert_into_crime_report(summary)
            #time.sleep(0.1)
            #print(f'added: {summary} \t from row #: {row}')
    if tipe == 2:
        summary_tuples = list(data.itertuples(index=False, name=None))
        #print(summary_tuples)
        for row, summary in enumerate(summary_tuples):
            T_Storage.insert_into_incident_report(summary)
            #time.sleep(0.0001)
            #print(f'added: {summary} \t from row #: {row}')
            if row == 100:
                break

    #data.to_sql("CrimeReport", connection, if_exists='append', index=False)
def getdatabase(tipe):
    #elements_in_db
    if tipe == 1:
        elements_in_db = pd.read_sql("SELECT * from CrimeReport", T_Storage.connect_to_db())
    elif tipe == 2:
        elements_in_db = pd.read_sql("SELECT * from Incident order by nature", T_Storage.connect_to_db())
    else:
        sys.exit(0)
    #type(elements_in_db)
    #print(elements_in_db)
    instances = list(elements_in_db['nature'])
    return instances
def status(db_data, row_len: int):
    for d in db_data:
        cnt = db_data.count(d)
        print(f'{d}|{cnt}')
        while cnt > 0:
            cnt -= 1
            db_data.pop(cnt)

def main(url, tipe=2):
    T_Storage.create_db()
    os.system('clear')      # create the new database
    #print(url)
    #fetchincidents(url)
    fetchincidents(url, tipe)
    df = getdatabase(tipe)
    #print(df)
    status(df.copy(), len(df))

if __name__ == "__main__":

    T_Storage.kill_db()                         # destroy the existing database
    os.system('clear')

    parser = argparse.ArgumentParser()

    parser.add_argument("--arrests", type=str, required=False,
                        help="The arrest summary url")

    parser.add_argument("--incidents", type=str, required=True,
                        help="The incident summary url")

    args = parser.parse_args()
    os.system('clear')
    if args.arrests:
        main(url=args.arrests, tipe=1)
    if args.incidents:
        main(url=args.incidents, tipe=2)
