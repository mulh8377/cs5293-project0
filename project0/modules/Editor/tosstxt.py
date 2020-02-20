import asyncio
import os
import re
import time

async def get_files(dir: str):
    storage = os.listdir(dir).copy()
    return storage
async def load_arrest_directory(dir="./data/txt/arrest/"):
    arr_txt = await get_files(dir)
    return arr_txt, dir
async def load_case_directory(dir="./data/txt/case/"):
    case_txt = await get_files(dir)
    return case_txt, dir
async def load_incident_directory(dir="./data/txt/incident/"):
    inc_txt = await get_files(dir)
    return inc_txt, dir
async def load_all():
    arr_files, arr_dir = await load_arrest_directory()

    case_files, case_dir = await load_case_directory()

    inc_files, inc_dir = await load_incident_directory()

    arr_flag = await parse_arrests(arr_files, arr_dir)
    case_flag = await parse_cases(case_files, case_dir)
    inc_flag = await parse_incidents(inc_files, inc_dir)
    return (arr_flag, case_flag, inc_flag)

async def parse_arrests(files: list, dir: str):
    summary = "ArrestSummary.txt"
    flag = False
    files.sort()
    if files[len(files) - 1] == summary:
        files.pop(len(files) - 1)
        flag = await remove_file(dir+summary)

    for a in files:
        await open_arrests(a, dir)
    return flag

async def parse_cases(files: list, dir: str):
    summary = "CaseSummary.txt"
    flag = False
    files.sort()
    if files[len(files) - 1] == summary:
        files.pop(len(files) - 1)
        flag = await remove_file(dir+summary)
    for a in files:
        await open_case(a, dir)
    return flag

async def parse_incidents(files: list, dir: str):
    summary = "IncidentSummary.txt"
    flag = False
    files.sort()
    if files[len(files) - 1] == summary:
        files.pop(len(files) - 1)
        flag = await remove_file(dir+summary)
    for a in files:
        await open_incidents(a, dir)
        break
    return flag
async def open_incidents(file_name, file_path):
    i_header = 'Date / Time\\nIncident Number\\nLocation\\nNature\\nIncident ORI\\n'
    with open(file_path + file_name, 'r') as fp:
        results = fp.readlines()
        time.sleep(0.1)
    fp.close()
    new = []
    for r in results:
        #print(r)
        new.append(r.replace(i_header, '-'))
    #print(new)
    r_flag = await remove_file(file_path + file_name)
    c_flag = await create_file(file_path + file_name, new)
    return r_flag == c_flag
    #return True
async def open_arrests(file_name, file_path):
    header = "Arrest Date / Time\\nCase Number\\nArrest Location\\nOffense\\nArrestee\\nArrestee Birthday\\nArrestee Address\\nCity\\nState\\nZip Code\\nStatus\\nOfficer\\n"
    with open(file_path + file_name, 'r') as fp:
        results = fp.readlines()
        time.sleep(0.1)
    fp.close()
    new = []
    for r in results:
        r.replace(header, '-')
        new.append(r.replace(header, '-'))

    r_flag = await remove_file(file_path + file_name)
    c_flag = await create_file(file_path + file_name, new)
    return r_flag == c_flag


async def open_case(file_name, file_path):
    c_header = 'Date / Time Reported\\nCase Number\\nLocation\\nOffense(s)\\nReporting Officer\\n'
    with open(file_path + file_name, 'r') as fp:
        results = fp.readlines()
        time.sleep(0.1)
    fp.close()
    new = []
    for r in results:
        #print(r)
        new.append(r.replace(c_header, '-'))
    #print(new)
    r_flag = await remove_file(file_path + file_name)
    c_flag = await create_file(file_path + file_name, new)
    return r_flag == c_flag
    #return True
async def remove_file(path):
    if os.path.isfile(path):
        os.remove(path)
        return True
    return False
async def create_file(path, data):
    if os.path.isfile(path) or data == None:
        return False
    else:
        with open(path, 'w+') as fp:
            fp.writelines(data)
        time.sleep(0.1)
        fp.close()
    if os.path.isfile(path):
        return True
async def main():
    await load_all()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())