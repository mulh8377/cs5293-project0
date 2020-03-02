import urllib.request
from os import *
import asyncio
import re
import PyPDF2
import numpy as np
from . import toss_download as td

def fetch_txt_all(dir="projects/cs5293-project0/data/txt/"):
    """

    :param dir:
    :return:
    """
    res = td.open_file()
    content = res[0].splitlines()
    #print(content)

    storage_pdf = []

    for count, element in enumerate(content, 0):
        print(f"file-number:{count}\t downloading:{element}")
        tag = re.split("/657/", element)
        tag[0] = count
        path = tag[1]
        storage_pdf.append(fetch_results(url=element, file=path))
    return storage_pdf

def fetch_results(url="", dir="/projects/cs5293-project0/data/pdf/", file="test.pdf"):
    urllib.request.urlretrieve(url, dir+file)
    return dir+file

def extract_results(data):
    """

    :param data:
    :return:
    """
    pdfReader = PyPDF2.PdfFileReader(data)
    print(pdfReader.numPages)
    page_obj = pdfReader.getPage(0)
    return page_obj.extractText().split('\n')

if __name__ == "__main__":
    pass
    #print(extract_results(fetch_results("http://normanpd.normanok.gov/filebrowser_download/657/2020-02-11%20Daily%20Arrest%20Summary.pdf")))
    #storage = fetch_all()
