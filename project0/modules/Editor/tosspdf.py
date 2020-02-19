import os
import sys
import PyPDF2
import pandas as pd
import numpy as np

def filterHeaderCase(data):
    headers = ["Date / Time Reported", "Case Number", "Location", "Offense(s)", "Reporting Officer"]
    if headers in data:
        return False
    else:
        return True
def filterHeaderIncidient(data):
    headers = ["Date / Time", "Incident Number", "Location", "Nature", "Incident ORI"]
    if headers in data:
        return False
    else:
        return True

def filterHeaderReport(data):
    headers = ["Arrest Date / Time", "Case Number", "Arrest Location",
               "Offense", "Arrestee", "Arrestee Birthday", "Arrestee Address",
               "City", "State", "Zip Code", "Status", "Officer"]
    if headers in data:
        return False
    else:
        return True
def transform_txt_case_summary(info):
    filter_cases = filter(filterHeaderCase, info)
    return filter_cases

def transform_txt_incident_summary(info):
    filter_incidents = filter(filterHeaderIncidient, info)
    return filter_incidents

def transform_txt_arrest_summary(info):
    filter_summaries = filter(filterHeaderReport, info)
    return filter_summaries


if __name__ == "__main__":
    print(f"tosspdf.py is designed to handle pdf reading, manipulation, and transformation")
    file = "/home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/data/pdf/2020-02-05 Daily Case Summary.pdf"