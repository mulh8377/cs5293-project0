import argparse
import tempfile
import sys
from os import *
import PyPDF2
import project0.modules.Crime.crime as Crime
import project0.modules.Editor.tosspdf as T_PDF
import project0.modules.Storage.tosstorage as T_Storage
import project0.modules.Utility.utility as T_Utility

def fetchincidents(url):
    data_loc = T_Utility.fetch_results(url)
    extract_incidents(data=data_loc)

def extract_incidents(data):
    pdfReader = PyPDF2.PdfFileReader(data)
    print(pdfReader.numPages)
    page_obj = pdfReader.getPage(0)

    print(page_obj.extractText())


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
