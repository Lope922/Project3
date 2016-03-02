import requests
from bs4 import BeautifulSoup

class PostalCode:

    def __init__(self):
        return self
an_easy_path = "C:/Users/Lope/PycharmProjects/Project3/Seperator/"
#does return zip code so need to assign a value equal to this


# set returns a zip so set it equal to a variable
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
# def zip_write_to_file(zipResponse):
#
#     #zip_warning_file = open("ziplistWarning.txt", mode="w+")
#     zip_response = zipResponse
#     htmldata = open(an_easy_path +"zip_code_response.html", mode="w+", buffering=1, encoding="UTF-8")
#
#     htmldata.write(str(zip_response))
#     htmldata.close()


# def read_from_file(zip_response):
#     f = open("zip_code_response.html","r")
#     # making soup from file contents instead of reduce server request narrowing query
#    # file_soup = BeautifulSoup(f, "html5lib")
#
#   #  print(file_soup.prettify())
# #todo see why i am getting the response 200 error


def make_zip_request(zip_from_file):
    try:
        urlforZip = 'http://www.zip-codes.com/zip-code-radius-finder.asp?zipMilesLow=0&zipMilesHigh=5&zip1={0}&Submit=Search'.format(zip_from_file)
        # make the request and store the response
        zip_response = requests.get(urlforZip)
        soup = BeautifulSoup(zip_response.content,"html5lib")
        return soup

    except Exception as ex:
        print("error trying to make web request for zip code details." + str(ex))

# this method reads the current file instead of the response as originally programmed
#todo this is the test data
def read_table_data(soup): # and make some soup out of it
    try:
       #  f = open("C:/Users/Lope/PycharmProjects/Project3/Seperator/zip_code_response.html", mode="r")
       #  # make some new soup for our application
       #  newSoup = BeautifulSoup(f, "html5lib")
       # # print(newSoup.prettify())
       #  f.close()
       #  # create the open and write file command
        list_of_zip_file_location = open("C:/Users/Lope/PycharmProjects/Project3/Seperator/zipList.txt", mode="w")
       #  # writ the zip codes to a file using the method below to extract data

        data = ""
        for lin in soup.find_all(name="td", class_="a", attrs="href", recursive=True):
            data += (lin.get_text("href")) + " "

        list_of_zip_file_location.writelines((data))
        list_of_zip_file_location.close()


        #writePostal_codes_to_file(zipresponse_content, list_of_zip_file_location)
       # return newSoup

    except IOError as ioerror:
        print("Problem trying to read in weather information" + str(ioerror))


''' :param BeautifulSoup object, and filewriter filewriter should contain an already opened directory and be able to write to the file'''
def writePostal_codes_to_file(ZipSoup, fileWriter):
    #zipdata = BeautifulSoup(ZipSoup, "html5lib")
    #fileWriter2 = open("C:/users/lope/pycharmProjects/Project3/Seperator/zipList.txt", mode="a")
    # zs = BeautifulSoup(ZipSoup.contents,"html5lib")
    data = ""
    # for lin in ZipSoup.find_all(name="td", class_="a", attrs="href", recursive=True):
    #
    #     data += (lin.get_text("href")) + " "
    #     print(data)
    # fileWriter.writelines((data))
    # fileWriter.close()
    # #return data
    ## print(lin.get_text("href"))
