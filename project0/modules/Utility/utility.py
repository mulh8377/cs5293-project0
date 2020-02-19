import urllib.request
from os import *
import asyncio
import re
import PyPDF2
import numpy as np
import project0.modules.Utility.toss_download as td

def fetch_all(dir="../../../data/txt/"):
    res = td.open_file()
    content = res[0].splitlines()
    print(content)

    storage_pdf = []

    for count, element in enumerate(content, 0):
        print(count, element)
        tag = re.split("/657/", element)
        tag[0] = count
        path = tag[1]
        storage_pdf.append(fetch_results(url=element, file=path))
    return storage_pdf

def fetch_results(url="", dir="/home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/data/pdf/", file="test.pdf"):
    urllib.request.urlretrieve(url, dir+file)
    return dir+file

def extract_results(data):
    pdfReader = PyPDF2.PdfFileReader(data)
    print(pdfReader.numPages)
    page_obj = pdfReader.getPage(0)
    return page_obj.extractText().split('\n')

if __name__ == "__main__":
    #print(extract_results(fetch_results("http://normanpd.normanok.gov/filebrowser_download/657/2020-02-11%20Daily%20Arrest%20Summary.pdf")))
    storage = fetch_all()
