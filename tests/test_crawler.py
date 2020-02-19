def test_wipe_data():
    import os
    import time
    os.chdir("/home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0")
    os.system("make wipe-data")
    time.sleep(1)
    empty_total = len(os.listdir("./data/txt/"))
    assert empty_total == 0