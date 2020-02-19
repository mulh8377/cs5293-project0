# dev-information
-----------------
Jared Mulhausen

- github        ->      mulh8377
- email         ->      jaredmulhausen@ou.edu
- student_id    ->      113358377

## Fields that Need Additional Editing
Case Number

Arrest Location

Offense

Arrestee

Arrestee Address

City

Status

Officer

# cs5293-project0
The Norman, Oklahoma police department regularly reports of incidents arrests and other activity. This project is meant to
showcase some recent skills we learned with the linux commands and python modules used to scrape data from the world wide web.
Norman PD keeps a monthly report of their activity online and our mission is to write a program that can parse this report 
and store it into a sqlite3 database.

## Useful Make Commands

- make crawl
    - gets the recent crime reports from the norman pd website
- make update
    - commits and pushes updates to github.
- make run **to do**

### Dependencies 
pandas==1.0.1
  - numpy [required: >=1.13.3, installed: 1.18.1]
  - python-dateutil [required: >=2.6.1, installed: 2.8.1]
    - six [required: >=1.5, installed: 1.14.0]
  - pytz [required: >=2017.2, installed: 2019.3]
pdfminer==20191125
  - pycryptodome [required: Any, installed: 3.9.6]
PyPDF2==1.26.0
pytest==5.3.5
  - attrs [required: >=17.4.0, installed: 19.3.0]
  - importlib-metadata [required: >=0.12, installed: 1.5.0]
    - zipp [required: >=0.5, installed: 2.2.0]
  - more-itertools [required: >=4.0.0, installed: 8.2.0]
  - packaging [required: Any, installed: 20.1]
    - pyparsing [required: >=2.0.2, installed: 2.4.6]
    - six [required: Any, installed: 1.14.0]
  - pluggy [required: >=0.12,<1.0, installed: 0.13.1]
    - importlib-metadata [required: >=0.12, installed: 1.5.0]
      - zipp [required: >=0.5, installed: 2.2.0]
  - py [required: >=1.5.0, installed: 1.8.1]
  - wcwidth [required: Any, installed: 0.1.8]
Scrapy==1.8.0
  - cryptography [required: >=2.0, installed: 2.8]
    - cffi [required: >=1.8,!=1.11.3, installed: 1.14.0]
      - pycparser [required: Any, installed: 2.19]
    - six [required: >=1.4.1, installed: 1.14.0]
  - cssselect [required: >=0.9.1, installed: 1.1.0]
  - lxml [required: >=3.5.0, installed: 4.5.0]
  - parsel [required: >=1.5.0, installed: 1.5.2]
    - cssselect [required: >=0.9, installed: 1.1.0]
    - lxml [required: Any, installed: 4.5.0]
    - six [required: >=1.5.2, installed: 1.14.0]
    - w3lib [required: >=1.19.0, installed: 1.21.0]
      - six [required: >=1.4.1, installed: 1.14.0]
  - protego [required: >=0.1.15, installed: 0.1.16]
    - six [required: Any, installed: 1.14.0]
  - PyDispatcher [required: >=2.0.5, installed: 2.0.5]
  - pyOpenSSL [required: >=16.2.0, installed: 19.1.0]
    - cryptography [required: >=2.8, installed: 2.8]
      - cffi [required: >=1.8,!=1.11.3, installed: 1.14.0]
        - pycparser [required: Any, installed: 2.19]
      - six [required: >=1.4.1, installed: 1.14.0]
    - six [required: >=1.5.2, installed: 1.14.0]
  - queuelib [required: >=1.4.2, installed: 1.5.0]
  - service-identity [required: >=16.0.0, installed: 18.1.0]
    - attrs [required: >=16.0.0, installed: 19.3.0]
    - cryptography [required: Any, installed: 2.8]
      - cffi [required: >=1.8,!=1.11.3, installed: 1.14.0]
        - pycparser [required: Any, installed: 2.19]
      - six [required: >=1.4.1, installed: 1.14.0]
    - pyasn1 [required: Any, installed: 0.4.8]
    - pyasn1-modules [required: Any, installed: 0.2.8]
      - pyasn1 [required: >=0.4.6,<0.5.0, installed: 0.4.8]
  - six [required: >=1.10.0, installed: 1.14.0]
  - Twisted [required: >=17.9.0, installed: 19.10.0]
    - attrs [required: >=17.4.0, installed: 19.3.0]
    - Automat [required: >=0.3.0, installed: 0.8.0]
      - attrs [required: >=16.1.0, installed: 19.3.0]
      - six [required: Any, installed: 1.14.0]
    - constantly [required: >=15.1, installed: 15.1.0]
    - hyperlink [required: >=17.1.1, installed: 19.0.0]
      - idna [required: >=2.5, installed: 2.8]
    - incremental [required: >=16.10.1, installed: 17.5.0]
    - PyHamcrest [required: >=1.9.0, installed: 2.0.0]
    - zope.interface [required: >=4.4.2, installed: 4.7.1]
      - setuptools [required: Any, installed: 45.2.0]
  - w3lib [required: >=1.17.0, installed: 1.21.0]
    - six [required: >=1.4.1, installed: 1.14.0]
  - zope.interface [required: >=4.1.3, installed: 4.7.1]
    - setuptools [required: Any, installed: 45.2.0]
