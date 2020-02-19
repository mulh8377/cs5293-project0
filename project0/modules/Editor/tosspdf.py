import os
import re
import time
import asyncio
import subprocess
import sys
import PyPDF2
import pandas as pd
import numpy as np


async def load_pdf_directory(dir_path="./data/pdf/"):

    files = os.listdir(path=dir_path)

    out_dir = "./data/txt/"

    case_files = [case for case in files if re.search(r"Case%", case)]
    await create_txt_directory(type='case', out_path=out_dir+'case/', files=case_files)
    #print(case_files)
    res_c = await transform_case_summary(pdf_path=dir_path, text_path=out_dir + 'case/',
                                 files=case_files)
    time.sleep(0.3)

    incident_files = [inc for inc in files if re.search(r"Incident%", inc)]
    await create_txt_directory(type='inc', out_path=out_dir + 'incident/', files=incident_files)
    #print(incident_files)
    res_i = await transform_incident_summary(pdf_path=dir_path, text_path=out_dir + 'incident/',files=incident_files)
    time.sleep(0.3)

    arrest_files = [arr for arr in files if re.search(r"Arrest%", arr)]
    await create_txt_directory(type='arr', out_path=out_dir + 'arrest/', files=arrest_files)
    res_arr = await transform_arrest_summary(pdf_path=dir_path, text_path=out_dir + 'arrest/', files=arrest_files)

    time.sleep(0.3)
    #print(arrest_files)

async def create_txt_directory(type, out_path, files):
    ext = ".txt"
    if type == "case":
        for f in files:
            #f.replace('.pdf', '.txt')
            fp = os.open(out_path+f+ext, os.O_CREAT)
            os.close(fp)
    elif type == "inc":
        for f in files:
            #f.replace('.pdf', '.txt')
            fp = os.open(out_path+f+ext, os.O_CREAT)
            os.close(fp)
    elif type == "arr":
        for f in files:
            #f.replace('.pdf', '.txt')
            fp = os.open(out_path+f+ext, os.O_CREAT)
            os.close(fp)
    else:
        return 0
    return 1

async def transform_case_summary(pdf_path, text_path, files):
    #filter_cases = filter(filterHeaderCase, info)
    ext = ".txt"
    for f in files:
        #pdf_file_pntr = os.open(pdf_path + f, os.O_RDONLY)
        pdf_reader = PyPDF2.PdfFileReader(pdf_path + f)
        total_pages = pdf_reader.numPages
        page_objects = []
        txt_info = []
        for cnt in range(0, total_pages, 1):
            page_objects.append(pdf_reader.getPage(cnt))
        for page in page_objects:
            txt_info.append(page.extractText())
        with open(text_path + f + ext, "w+") as fp:
            for txt in txt_info:
                fp.write(repr(txt))
            fp.close()
    return 1

async def transform_incident_summary(pdf_path, text_path, files):
    #filter_cases = filter(filterHeaderCase, info)
    ext = ".txt"
    for f in files:
        #pdf_file_pntr = os.open(pdf_path + f, os.O_RDONLY)
        pdf_reader = PyPDF2.PdfFileReader(pdf_path + f)
        total_pages = pdf_reader.numPages
        page_objects = []
        txt_info = []
        for cnt in range(0, total_pages, 1):
            page_objects.append(pdf_reader.getPage(cnt))
        for page in page_objects:
            txt_info.append(page.extractText())
        with open(text_path + f + ext, "w+") as fp:
            for txt in txt_info:
                fp.write(repr(txt))
            fp.close()
    return 1

async def transform_arrest_summary(pdf_path, text_path, files):
    ext = ".txt"
    for f in files:
        #pdf_file_pntr = os.open(pdf_path + f, os.O_RDONLY)
        pdf_reader = PyPDF2.PdfFileReader(pdf_path + f)
        total_pages = pdf_reader.numPages
        page_objects = []
        txt_info = []
        for cnt in range(0, total_pages, 1):
            page_objects.append(pdf_reader.getPage(cnt))
        for page in page_objects:
            txt_info.append(page.extractText())
        with open(text_path + f + ext, "w+") as fp:
            for txt in txt_info:
                fp.write(repr(txt))
            fp.close()
    return 1

async def main():
    await load_pdf_directory()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())