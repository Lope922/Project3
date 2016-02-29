import requests
from bs4 import BeautifulSoup


# all of this is done in HTML
def read_zipcode_response():

    zipinfo = (open('users_zip_code.txt', 'r'))
    # read the first line from the file that contains the zip
    a = zipinfo.readline()
    #print("here is the zipinfo " +a)
    return a

# pass in the zip code retrieved from file
def make_zip_request(zip_from_file):
    try :
        urlforZip = 'http://www.zip-codes.com/zip-code-radius-finder.asp?zipMilesLow=0&zipMilesHigh=10&zip1={0}&Submit=Search'.format(zip_from_file)
        #print("here is the url to test by clicking on it " + urlforZip)

        # make the request and store the response
        zip_response = requests.get(urlforZip)

        # turn it into soup
        zip_soup = BeautifulSoup(zip_response.content, "html5lib")
        #zip_soup.prettify()
       # z = zip_soup.find_all("td", "a", limit=10)
        # before it's turned into beautify soup print to see what it looks like
       # print(z)


        smallerChunk = zip_soup.find("a", {'href = '})
        print(str(smallerChunk))

        #regex =  zip_soup.attribselect_re("<td class = a><a href=>")
        #print(str(regex))
        #chunk_tag = zip_soup.find("<td class = a><a href=>")
        #print("the new style : " + str(chunk_tag))


        # from the response read the list of zips and add them to a list of radius' to alert

        #todo trying to find all bs and their hrefs in the zipcode response
        # read to the file that visual studio used to record the users input and generate a request for some new info based on the request.

#        zip = 0

        # open a file in the given path with the directory open it with the read only privleges.
        #f = open('workfile', 'r')


        # website to possibly use and make use of zipcode information. http://www.zip-codes.com/zip-code-radius-finder.asp
    except Exception as ex:
        print("error trying to make web request for zip code details." + ex)



#todo add some sort of trigger to initiate the get zip response method. IF FILE is not empty
#todo if file is empty halt the program and exit. Display a message letting the user know what went wrong.


#todo look into async to see if the two programs need to be setup to communicate with eachother.

