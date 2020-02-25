import os
import subprocess
import asyncio

async def create_directories():
    arrest_csv = "./data/csv/arrest/"
    case_csv = "./data/csv/case/"
    incident_csv = "./data/csv/incident/"
    if not os.path.isdir(incident_csv):
        os.mkdir(incident_csv)
    #subprocess.call(['touch', incident_csv + 'clean.csv'])
    if not os.path.isdir(case_csv):
        os.mkdir(case_csv)
    #subprocess.call(['touch', clean.csv'])
    if not os.path.isdir(arrest_csv):
        os.mkdir(arrest_csv)
    #subprocess.call(['touch', arrest_csv + 'clean.csv'])

    c_f = await move_case_summary(case_csv)
    i_f = await move_inc_summary(incident_csv)
    a_f = await move_arr_summary(arrest_csv)
    return c_f, i_f, a_f
async def move_case_summary(dir):
    assert os.path.isdir(dir)
    subprocess.call(['cp', './data/txt/case/CaseSummary.txt', dir])
    subprocess.call(['mv', './data/csv/case/CaseSummary.txt', './data/csv/case/Summary.txt'])
    return os.path.isfile(dir + "Summary.txt")
async def move_inc_summary(dir):
    assert os.path.isdir(dir)
    subprocess.call(['cp', './data/txt/incident/IncidentSummary.txt', dir])
    subprocess.call(['mv', './data/csv/incident/IncidentSummary.txt', './data/csv/incident/Summary.txt'])
    return os.path.isfile(dir + "Summary.txt")
async def move_arr_summary(dir):
    assert os.path.isdir(dir)
    FILE = "CleanSummary.txt"
    if os.path.isfile(dir + FILE):
        os.remove(dir + FILE)
    subprocess.call(['cp', './data/txt/arrest/ArrestSummary.txt', dir])
    subprocess.call(['mv', './data/csv/arrest/ArrestSummary.txt', './data/csv/arrest/Summary.txt'])
    stuff = []
    flag = True
    if os.path.isfile(dir + "Summary.txt"):
        with open('./data/csv/arrest/Summary.txt', 'r') as arr:
            stuff = arr.readlines()

        arr.close()
        #print(stuff)
        for s in stuff:
            info = s.split(';')
            for i in info:
               flag = await create_clean_file(dir=dir, field=i)
    return flag

async def create_clean_file(dir, field):
    FILE = "CleanSummary.txt"
    #if os.path.isfile(dir + FILE):
        #os.remove(dir + FILE)
    if len(field) > 0:
        with open(dir + FILE, 'a+') as cln:
            cln.write(field)
            cln.write('\n')
        cln.close()

        return True
        #await sum_transform_arr()
    else:
        print('failed to write to field')
        return False

async def load_summaries(case_file, inc_file, arr_file):
    if case_file:
        await sum_transform_case()
    if inc_file:
        await sum_transform_inc()
    if arr_file:
        await sum_transform_arr()
async def sum_transform_case(path="./data/csv/case/Summary.txt"):
    print(path)
async def sum_transform_arr(path="./data/csv/arrest/CleanSummary.txt"):
    """
    sed -i -e 's/-//g' data/csv/arrest/Summary.txt ## gets rid of '-'

    sed -i -e 's/ /\n/g' data/csv/arrest/Summary.txt ## gets rid of ' \n'

    sed -i -e 's/Daily//g' data/csv/arrest/Summary.txt ## gets rid of 'Daily'
    sed -i -e 's/Arrest//g' data/csv/arrest/Summary.txt
    sed -i -e 's/Activity//g' data/csv/arrest/Summary.txt

    sed -i -e 's/(Public).nNORMAN//g' data/csv/arrest/Summary.txt
    sed -i -e 's/POLICE//g' data/csv/arrest/Summary.txt
    sed -i -e 's/DEPARTMENT.n'//g' data/csv/arrest/Summary.txt

    """
    #print(path)
    subprocess.call(['bash', 'scripts/arrest-csv-clean.sh'])
    if os.path.isfile(path):
        with open(path) as fp:
            lines = fp.readlines()
            for l in lines:
                cleanr = l.replace('\\n', '\\t')
                await create_clean_csv_arr(clean_line=cleanr)
        fp.close()
        subprocess.call(['bash', 'scripts/arrest-csv.sh'])
        await analyze_arrest_csv()

async def create_clean_csv_arr(clean_line: str, FILE="./data/csv/arrest/clean.csv"):
    print(repr(clean_line))
    better_line = clean_line.replace(' \\t', ' ')
    if len(better_line) > 0:
        field_line = better_line.replace('\\t', ', ')
        with open(FILE, 'a+') as cln:
            print(field_line)
            cln.write(field_line)
            #zcln.write('\n')
            print("file opened")
        cln.close()

async def analyze_arrest_csv(FILE="./data/csv/arrest/clean.csv"):

    with open(FILE, 'r') as rdr:
        rows = rdr.readlines()
        for r in rows:
            total_commas_in_row = comma_counter(r)
            print(f'commas: {total_commas_in_row} \t info {r}')
    rdr.close()

async def sum_transform_inc(path="./data/csv/arrest/Summary.txt"):
    print(path)

def comma_counter(field: str):
    total = 0
    for f in field:
        if f == ',':
            total += 1
    return total
async def main():
    c, i, a = await create_directories()
    await load_summaries(c, i, a)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())