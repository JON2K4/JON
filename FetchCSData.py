import urllib.request

def fetchPY(url, name, location="/home/student/Dump/"):
    serverFilename = urlFileName(url)
    print("REQUEST: Mode 1 (.py) for {} @ {} to {}".format(serverFilename, url, location+name))
    urllib.request.urlretrieve(url, location+name)

def fetchTXT(url, name, location="/home/student/Dump/"):
    serverFilename = urlFileName(url)
    print("REQUEST: Mode 0 (.txt) for {} @ {} to {}".format(serverFilename, url, location+name))
    urllib.request.urlretrieve(url, location+name)

def urlFileName(url):
    indexOfFilename = url.rfind("/") + 1

    return url[indexOfFilename:]

def promptFetch(mode):
    url = input("Please provide a url: \n")
    path = input("Please provide a path: \n")
    fileName = input("Please provide a file name: \n")

    if mode == 0:
        fetchTXT(url=url, name=fileName, location=path)

    if mode == 1:
        fetchPY(url=url, name=fileName, location=path)


if __name__ == "__main__":
    promptFetch(0)
