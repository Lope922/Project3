import requests
from bs4 import BeautifulSoup
import os.path


def initialize_directory():
    if os.path.isdir("Response_Info"):
        print("we are good the path to store the response info in is made.")
        open("C:/Users/CaLs_Rig/PycharmProjects/Project3/Program/Response_info/floodinfo.txt", mode="w+")
    else:
        os.mkdir("Response_info")



def get_basic_flood_info():

# create request to the floodsafety website , reads response in html5
    try:
        #generate the reqeust
        r = requests.get("http://www.floodsafety.noaa.gov/", "html5lib")

        #let make some soup
        soup = BeautifulSoup(r.content, "html5lib")

        #narrow down the tables
        tables = soup.select("tr")

        # for testing purposes
        #print(tables[1].find("p"))

        # grab the items in index of 1 and find ones that start with p
        info = tables[1].find("p")

        #todo remove <p> format from the text

        #flood details to be displayed in visual studio app stored here
        Flood_deets = str(info)


        return Flood_deets
    #try and catch some errors not all yet
    except requests.HTTPError as bad_request:
        print("there as an error trying to make the web request. Check you connection and try again." + bad_request)
    except Exception as ex:
        print("There has been an error. Source may have changed its layout, check source code\nMessage details" + ex)

# todo strip the hypertext format from reply
# store this either into a file or a variable to write onto a form.


# pass in the response from the web to save to a file to display in another program.
def record_flood_info(responseText):
    #todo write to a file
    save_path = "C:/Users\CaLs_Rig/PycharmProjects/Project3/Program/Response_info/"
    file_name = "floodinfo.txt"
    save = open(save_path + file_name, "a")
    info = responseText
    # convert its contents to string fromat
    save.write(str(info))
    # close the file so that other resources can use it
    save.close()

    #todo read from a file to make the next request using the zip provided through a different program.


# all of this is done in HTML
def read_zipcode_response():

    zipinfo = (open('C:/Users/CaLs_Rig/PycharmProjects/Project3/Program/Response_info/users_zip_code.txt', 'r'))

    # read the first line from the file that contains the zip
    a = zipinfo.readline()
    #print("here is the zipinfo " +a)
    zipinfo.close()
    return a


#outer html for zip tag <a href="/zip-code/63139/zip-code-63139.asp">63139</a>
# pass in the zip code retrieved from file
#todo rewrite and split into two methods , one that makes the request and another that writes the request

# needs the file location/name passed in for testing purposes only
#Only need to run this when the zip changed
def zip_write_to_file():
    htmldata = open("zip_code_response.html", mode="w+", buffering=1, encoding="UTF-8")

    htmldata.write(str(zip_response.text))
    htmldata.close()
    f = open("zip_code_response.html","r")
    # making soup from file contents instead of reduce server request narrowin query
    file_soup = BeautifulSoup(f, "html5lib")

    print(file_soup.prettify())

def read_from_file():






def make_zip_request(zip_from_file):
    try:
        urlforZip = 'http://www.zip-codes.com/zip-code-radius-finder.asp?zipMilesLow=0&zipMilesHigh=5&zip1={0}&Submit=Search'.format(zip_from_file)

        # make the request and store the response
        zip_response = requests.get(urlforZip)

        # turn it into soup #todo NOTE DO NOT DELETE ZIP SOUP changing to read from file
        zip_soup = BeautifulSoup(zip_response.content, "html5lib")
        # started with this
        # achunk = zip_soup.select("td.a")
       # zip_soup.find
       # achunk = zip_soup.find_all("td.a", class_="a",attrs="a href=",recursive=True) # todo modify this to narrow down results.
        #bchunk = zip_soup.find_all("td", class_="a", attrs="href", recursive=True)
        #print("Here is be chunk " + str(bchunk))# todo modify this to narrow down results.

        # if i can strip its contents i can search using it as a regular expression
        #placeIwant = bchunk[1].find_all("a")



        # print("\n\n\n")
        # for each_spot in bchunk:
        #     print(str(each_spot))

        p#rint("\n\n this is the chunk i sliced " + str(placeIwant))

       # print("Here is a chunk" + str(achunk))
       # print("_______________-----------------____________" + str(bchunk))

        # website to possibly use and make use of zipcode information. http://www.zip-codes.com/zip-code-radius-finder.asp
    except Exception as ex:
        print("error trying to make web request for zip code details." + str(ex))


# todo add some sort of trigger to initiate the get zip response method. IF FILE is not empty
# todo look into async to see if the two programs need to be setup to communicate with eachother.
# todo write a method that check the file size of the zip code response before it runs read zip code response

# this requires program to have access and import os.path
def remove_old_files():
    os.rmdir("C:/Users/CaLs_Rig/PycharmProjects/Project3/Program/Response_info")


# this method checks that a file has been made in Visual studio, and tries creates a request for the zip codes within a
# given area
def chk_file():
    if os.path.isfile('C:/Users/CaLs_Rig/PycharmProjects/Project3/Program/Response_info/users_zip_code.txt'):
    #if os.path.isfile('/Program/Response_info/users_zip_code.txt'):
        print('i have found the file')
    # may want to check length
    #    print("The file contains some bytes")
    #if the path exists return true
        True

    else:
        print("file could not be found or has not been created.")
    #need to double check this logic
        False

# ----------------  program stats here -----------------
initialize_directory()

# create the flood info from national weather service website
reply = get_basic_flood_info()

# save the info to a file to use later
record_flood_info(reply)
#if chk_file():
     # if there are contents in the file then read them , and make request for list of zips , and return website
users_zip = read_zipcode_response()
make_zip_request(users_zip)
if reply is None:
      print("There was an error trying to retrieve the flood details")
else:
      print("Could not locate the proper file to process")
print("program will now exit")
# this isn't working yet, but not major
#remove_old_files()
exit(0)
