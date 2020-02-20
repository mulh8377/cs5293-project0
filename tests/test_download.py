
def test_download_one():
    import project0.modules.Utility.utility as Ut
    import os
    storage = Ut.fetch_results(url="http://normanpd.normanok.gov/filebrowser_download/657/2020-02-11%20Daily%20Incident%20Summary.pdf",
                               file="test.pdf")
    current_directory_size = os.listdir("./data/pdf/")
    assert current_directory_size.__contains__("test.pdf")


def test_download_all():
    import project0.modules.Utility.utility as Ut
    import os
    storage = Ut.fetch_txt_all()
    #assert len(os.listdir('./data/pdf/')) > 0
    storage = os.listdir('./data/pdf/')
    assert len(storage) > 0
    for s in storage:
        assert os.path.splitext(s)[1] == '.pdf'



