import urllib.request

def fetch_url(dir="filebrowser_download", name="", ext=".pdf"):
    domain = "http://normanpd.normanok.gov/"
    directory = dir + "/"
    file_name = name + ext + "/"
    return domain + directory + file_name 

def fetch_results(url=""):
    dir = "/home/mulh8377/Courses/TextAnalyis/projects/cs5293-project0/data/pdf/test.pdf"
    urllib.request.urlretrieve(url, dir)
    return dir
if __name__ == "__main__":
    #fetch_results("http://normanpd.normanok.gov/filebrowser_download/657/2020-02-11%20Daily%20Incident%20Summary.pdf")
    pass