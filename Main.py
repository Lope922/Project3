import requests
from bs4 import BeautifulSoup


def get_basic_flood_info():

# create request to the floodsafety website , reads response in html5
    try:
        r = requests.get("http://www.floodsafety.noaa.gov/", "html5lib")


        soup = BeautifulSoup(r.content, "html5lib")
        tables = soup.select("tr")

        # for testing purposes
        #print(tables[1].find("p"))

        info = tables[1].find("p")
        #flood details to be displayed in visual studio app stored here
        Flood_deets = str(info)

        return Flood_deets
    #try and catch any errors and
    except requests.HTTPError as bad_request:
        print("there as an error trying to make the web request. Check you connection and try again.")
    except Exception as ex:
        print("There has been an error. Source may have changed its layout, check source code\nMessage details" + ex)


#todo strip the hypertext format from phrase
# store this either into a file or a variable to write onto a form.

# pass in the response from the web to save to a file to display in another program.
def record_flight_info(responseText):
    #todo write to a file
    s = open('floodinfo.txt', "a")
    info = responseText
    # convert its contents to string fromat
    s.write(str(info))
    # close the file so that other resources can use it
    s.close()
    #todo read from a file to make the next request using the zip provided through a different program.


def read_zipcode_response():

    # read to the file that visual studio used to record the users input and generate a request for some new info based on the request.

    zip = 0

    # open a file in the given path with the directory open it with the read only privleges.
    #f = open('workfile', 'r')


    # website to possibly use and make use of zipcode information. http://www.zip-codes.com/zip-code-radius-finder.asp


# program stats here

response = get_basic_flood_info()
if response is None:
    print("There was an error trying to retrieve the flood details")
else:
    record_flight_info(response)
#todo look into async to see if the two programs need to be setup to communicate with eachother.
