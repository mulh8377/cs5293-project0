import argparse
import tempfile
import sys
from os import *
import PyPDF2
import modules.Crime.crime as Crime
import modules.Editor.tosspdf as T_PDF
import modules.Storage.tosstorage as T_Storage
import modules.Utility.utility as T_Utility

def fetchincidents(url):
    if url == "all":
        data_loc = T_Utility.fetch_all()
    else:
        data_loc = T_Utility.fetch_results(url)
    extractincidents(data=data_loc)

def extractincidents(data):
    print("create the pdf file here")
    #results = T_Utility.extract_results(data)


def main(url):
    print(url)
    #fetchincidents(url)
    fetchincidents(url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--arrests", type=str, required=True,
                        help="The arrest summary url")

    args = parser.parse_args()

    if args.arrests:
        main(args.arrests)
