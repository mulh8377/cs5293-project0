import argparse
import tempfile
import sys
from os import *
import PyPDF2
import time
import subprocess
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


def main(url):
    T_Storage.create_db()                       # create the new database
    #print(url)
    #fetchincidents(url)
    fetchincidents(url)


if __name__ == "__main__":
    T_Storage.kill_db()                         # destroy the existing database

    parser = argparse.ArgumentParser()

    parser.add_argument("--arrests", type=str, required=True,
                        help="The arrest summary url")

    args = parser.parse_args()

    if args.arrests:
        main(args.arrests)
