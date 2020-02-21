import os
import subprocess
import asyncio

async def create_directories():
    arrest_csv = "./data/csv/arrest/"
    case_csv = "./data/csv/case/"
    incident_csv = "./data/csv/incident/"
    if not os.path.isdir(incident_csv):
        os.mkdir(incident_csv)
    if not os.path.isdir(case_csv):
        os.mkdir(case_csv)
    if not os.path.isdir(arrest_csv):
        os.mkdir(arrest_csv)

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
    subprocess.call(['cp', './data/txt/arrest/ArrestSummary.txt', dir])
    subprocess.call(['mv', './data/csv/arrest/ArrestSummary.txt', './data/csv/arrest/Summary.txt'])
    return os.path.isfile(dir + "Summary.txt")

async def load_summaries(case_file, inc_file, arr_file):
    if case_file:
        await sum_transform_case()
    if inc_file:
        await sum_transform_inc()
    if arr_file:
        await sum_transform_arr()
async def sum_transform_case(path="./data/csv/case/Summary.txt"):
    print(path)
async def sum_transform_arr(path="./data/csv/arrest/Summary.txt"):
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
    print(path)
    subprocess.call(['bash', 'scripts/arrest-csv-clean.sh'])
async def sum_transform_inc(path="./data/csv/arrest/Summary.txt"):
    print(path)
async def main():
    c, i, a = await create_directories()
    await load_summaries(c, i, a)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())