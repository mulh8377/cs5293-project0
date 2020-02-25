import argparse
import tempfile
import sys
from os import *
import PyPDF2
import time
import subprocess
import pandas as pd
import modules.Crime.crime as Crime
import modules.Editor.tosspdf as T_PDF
import modules.Storage.tosstorage as T_Storage
import modules.Utility.utility as T_Utility

def fetchincidents(url):
    if url == "all":                            # default parameter if make run-project is called.
        data_loc = T_Utility.fetch_txt_all()
    else:
        data_loc = T_Utility.fetch_results(url) # alternative if user runs pipenv run python project0/main.py --arrests <url>
    extractincidents(data=data_loc)

def extractincidents(data):
    #print("extract the pdf fields here")
    """
    TODO:
    """
    subprocess.call(['bash', './scripts/transform-pdf.sh'])
    time.sleep(0.3)
    #subprocess.call(['cat', './data/txt/arrest/ArrestSummary.txt'])
    #results = T_Utility.extract_results(data)
    data = pd.read_csv('./data/csv/arrest/arrest.csv')
    #print(data)
    #data.to_sql('CrimeReport', T_Storage.connect_to_db(), if_exists='append', index=False)
    importincidents(data)
def importincidents(data):
    #print(data)
    #connection = T_Storage.connect_to_db()
    #print(connection)
    summary_tuples = list(data.itertuples(index=False, name=None))
    #print(summary_tuples)
    for row, summary in enumerate(summary_tuples):
        T_Storage.insert_into_crime_report(summary)
        time.sleep(0.1)
        print(f'added: {summary} \t from row #: {row}')
    #data.to_sql("CrimeReport", connection, if_exists='append', index=False)
def getdatabase():
    elements_in_db = pd.read_sql("SELECT * from CrimeReport", T_Storage.connect_to_db())
    return elements_in_db
    #print(elements_in_db)
def status(dataframe: pd.DataFrame, row_len: int, total_out=1):
    print(row_len, total_out)
def main(url):
    T_Storage.create_db()                       # create the new database
    #print(url)
    #fetchincidents(url)
    fetchincidents(url)
    CrimeReport_DF = getdatabase()
    status(CrimeReport_DF, CrimeReport_DF.size)

if __name__ == "__main__":
    T_Storage.kill_db()                         # destroy the existing database

    parser = argparse.ArgumentParser()

    parser.add_argument("--arrests", type=str, required=True,
                        help="The arrest summary url")

    args = parser.parse_args()

    if args.arrests:
        main(args.arrests)
