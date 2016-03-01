import requests
from bs4 import BeautifulSoup
import os.path

# trying to refactor as a class that only reads and uses the flood data  & should be able to be adapted easily for snow
class Part1:
    CONSTANT_PATH = "relative path part1"
    CONSTANT_PATH_PART_2 = "relative path part2"
    def __init__(self):
        return self


# returns a paragraph to print later
def request_basic_weather_info():

# create request to the floodsafety website , parse in html
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

        #details to be displayed in visual studio app stored here
        the_deets = str(info)


        # store this either into a file or a variable to write onto a form.
        return the_deets

    #try and catch some errors sure if all are covered not all yet
    except requests.HTTPError as bad_request:
        print("there as an error trying to make the web request. Check you connection and try again." + bad_request)
    except Exception as ex:
        print("There has been an error. Source may have changed its layout, check source code\nMessage details" + ex)

    #todo once program is built write some unit tests


 # pass in the response from the web to save to a file to display in another program.
    '''Requires a request.content to be passed in'''
def save_warning_info(the_deets):
    # once i find a more effienct way of doing this adjust path # todo <-----=====
    save_path = "C:/Users\CaLs_Rig/PycharmProjects/Project3/Program/Response_info/"
    file_name = "BadWeatherInfo.txt"
    save = open(save_path + file_name, "a")
    #info
    # convert its contents to string fromat
    save.write(str(the_deets))
    # close the file so that other resources can use it
    save.close()
    print("file has been written check directory")

    # next make request using the zip provided through a different program.

    # todo add some sort of trigger to initiate the get zip response method. IF FILE is not empty
    # todo look into async to see if the two programs need to be setup to communicate with eachother.
    # todo write a method that check the file size of the zip code response before it runs read zip code response

    # ----------------  program stats here -----------------
#
#
# initialize_directory()
#
# # create the flood info from national weather service website
# reply = get_basic_flood_info()
#
# # save the info to a file to use later
# record_flood_info(reply)
# #if chk_file():
#      # if there are contents in the file then read them , and make request for list of zips , and return website
# users_zip = get_zipcode_response()
# zipResponse = make_zip_request(users_zip)
# read_from_file(zipResponse)
# todo consider putting this in a finally block
# if reply is None:
#       print("There was an error trying to retrieve the flood details")
# else:
#       print("Could not locate the proper file to process")
# print("program will now exit")
# # this isn't working yet, but not major
# #remove_old_files()
# exit(0)
