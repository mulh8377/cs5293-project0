import asyncio
import os
import re
import time

async def get_files(dir: str):
    """

    :param dir:
    :return: a list of txt_file paths
    """
    storage = os.listdir(dir).copy()
    return storage
async def load_arrest_directory(dir="./data/txt/arrest/"):
    """

    :param dir: location of arrest txt files
    :return: a list of txt_paths and the directory
    """
    arr_txt = await get_files(dir)
    return arr_txt, dir
async def load_case_directory(dir="./data/txt/case/"):
    """

    :param dir: location of case txt files
    :return: a list of txt_paths and the directory
    """
    case_txt = await get_files(dir)
    return case_txt, dir
async def load_incident_directory(dir="./data/txt/incident/"):
    """

    :param dir: location of incident txt files
    :return: a list of txt_paths and the directory
    """
    inc_txt = await get_files(dir)
    return inc_txt, dir
async def load_all():
    arr_files, arr_dir = await load_arrest_directory()      # get arrests

    case_files, case_dir = await load_case_directory()      # get cases

    inc_files, inc_dir = await load_incident_directory()    # get incidents

    arr_flag = await parse_arrests(arr_files, arr_dir)      # parse arrests
    case_flag = await parse_cases(case_files, case_dir)     # parse cases
    inc_flag = await parse_incidents(inc_files, inc_dir)    # parse incidents
    return (arr_flag, case_flag, inc_flag)

async def parse_arrests(files: list, dir: str):
    """

    :param files: paths to files
    :param dir:  location of files
    :return: bool
    """
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
    """

    :param files: paths to files
    :param dir:  location of files
    :return: bool
    """
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
    """

    :param files: paths to files
    :param dir:  location of files
    :return: bool
    """
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
    """

    :param file_name: file to open
    :param file_path: the location of the file
    :return: bool
    """

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
    r_flag = await remove_file(file_path + file_name)           ## removes exisiting file
    c_flag = await create_file(file_path + file_name, new)      ## creates new file
    return r_flag == c_flag
    #return True
async def open_arrests(file_name, file_path):
    """

    :param file_name: file to open
    :param file_path: the location of the file
    :return: bool
    """
    header = "Arrest Date / Time\\nCase Number\\nArrest Location\\nOffense\\nArrestee\\nArrestee Birthday\\nArrestee Address\\nCity\\nState\\nZip Code\\nStatus\\nOfficer\\n"
    with open(file_path + file_name, 'r') as fp:
        results = fp.readlines()
        time.sleep(0.1)
    fp.close()
    new = []
    for r in results:
        r.replace(header, '-')
        new.append(r.replace(header, '-'))

    r_flag = await remove_file(file_path + file_name) ## remover
    c_flag = await create_file(file_path + file_name, new) ## creater
    return r_flag == c_flag


async def open_case(file_name, file_path):
    """

    :param file_name: file to open
    :param file_path: the location of the file
    :return: bool
    """
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
    r_flag = await remove_file(file_path + file_name)           # remover
    c_flag = await create_file(file_path + file_name, new)      # creater
    return r_flag == c_flag
    #return True
async def remove_file(path):
    """
    :param path:
    :return: bool
    """
    if os.path.isfile(path):
        os.remove(path)
        return True
    return False
async def create_file(path, data):
    """

    :param path:    location for the creation
    :param data:    lines to be written to path
    :return:        bool
    """
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