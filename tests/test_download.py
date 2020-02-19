
def test_download_one():
    import project0.modules.Utility.utility as Ut
    import os
    os.remove("./data/pdf/test.pdf")
    current_directory_size = len(os.listdir("./data/pdf/"))
    storage = Ut.fetch_results(url="http://normanpd.normanok.gov/filebrowser_download/657/2020-02-11%20Daily%20Incident%20Summary.pdf",
                               file="test.pdf")
    new_directory_size = len(os.listdir("./data/pdf/"))
    assert current_directory_size == new_directory_size


def test_download_all():
    import project0.modules.Utility.utility as Ut
    import os
    os.remove("./data/pdf/test.pdf")
    storage = Ut.fetch_all()
    assert len(storage) == len(os.listdir("./data/pdf/"))



