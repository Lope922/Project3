import requests
from bs4 import BeautifulSoup

class PostalCode:

    def __init__(self):
        return self
an_easy_path = "C:/Users/Lope/PycharmProjects/Project3/Seperator/"
#does return zip code so need to assign a value equal to this
''' :parameter set equal to something '''
def get_zipcode_response():
    #todo adjust this path as well
    zipinfo = (open(an_easy_path + 'users_zip_code.txt', 'r'))

    # read the first line from the file that contains the zip that's all we need
    a = zipinfo.readline()
    #print("here is the zipinfo " +a)
    zipinfo.close()
    return a

# pass in the zip code retrieved from file needs the file location/name passed in for testing purposes only
#Only need to run this when the zip changed
def zip_write_to_file(zipResponse):

    #zip_warning_file = open("ziplistWarning.txt", mode="w+")
    zip_response = zipResponse
    htmldata = open(an_easy_path +"zip_code_response.html", mode="w+", buffering=1, encoding="UTF-8")

    htmldata.write(str(zip_response))
    htmldata.close()


def read_from_file(zip_response):
    f = open("zip_code_response.html","r")
    # making soup from file contents instead of reduce server request narrowing query
    file_soup = BeautifulSoup(f, "html5lib")

    print(file_soup.prettify())

def make_zip_request(zip_from_file):
    try:
        urlforZip = 'http://www.zip-codes.com/zip-code-radius-finder.asp?zipMilesLow=0&zipMilesHigh=5&zip1={0}&Submit=Search'.format(zip_from_file)
        # make the request and store the response
        zip_response = requests.get(urlforZip)
        return zip_response

    except Exception as ex:
        print("error trying to make web request for zip code details." + str(ex))

# this method reads the current file instead of the response as originally programmed
#todo this is the test data
def read_table_data(): # and make some soup out of it
    try:
        f = open("C:/Users/Lope/PycharmProjects/Project3/Seperator/zip_code_response.html", mode="r")
        # make some new soup for our application
        newSoup = BeautifulSoup(f, "html5lib")
        f.close()
        return newSoup

    except IOError as ioerror:
        print("Problem trying to read in weather information" + str(ioerror))



#print(newSoup.prettify())

# extracts the text i want but there are so many extra strings still need to narrow it down
# for link in newSoup.find_all("a"):
#     print(link.get_text("href"))
#     #print(link.get("href"))

''' :param BeautifulSoup object, and filewriter filewriter should contain an already opened directory and be able to write to the file'''
def writePostal_codes_to_file(ZipSoup, fileWriter):

    for lin in ZipSoup.find_all(name="td", class_="a", attrs="href", recursive=True):
        a = " "
        a += (lin.get_text("href")) + " "
        fileWriter.writelines(a)
    return a
    ## print(lin.get_text("href"))
