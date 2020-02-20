def test_pdfexecutionspeed():
    import time
    import subprocess
    start = time.time()
    subprocess.call(['pipenv', 'run', 'python', 'project0/modules/Editor/tosspdf.py'])
    end = time.time()
    print(end-start)
def test_txtexecutionspeed():
    import time
    import subprocess
    start = time.time()
    subprocess.call(['pipenv', 'run', 'python', 'project0/modules/Editor/tosstxt.py'])
    end = time.time()
    print(end-start)
def test_csvexecutionspeed():
    import time
    import subprocess
    start = time.time()
    subprocess.call(['pipenv', 'run', 'python', 'project0/modules/Editor/tosscsv.py'])
    end = time.time()
    print(end-start)