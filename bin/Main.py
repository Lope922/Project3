import requests
from bs4 import BeautifulSoup
import os.path
import Part1 as Weather
import bin.Part2 as PostalCode
import FileManager.FileManagerClass as fm





def Main():

    an_easy_path = "C:/Users/Lope/PycharmProjects/Project3/Seperator/"

    fm.chk_dir_exists()
    # request information from National Weather Service
    response = Weather.request_basic_weather_info()

        # if response is not nothing
    if response is not None:
        Weather.save_warning_info(response)
        #todo here is where i would like to insert the break/check for call back to retrieve input from other app

        # read zip code file
        # todo if no such file exists halt for 6 or so seconds and wait for that process to complete
        # get user input from first form
        user_zip_input = PostalCode.get_zipcode_response()
        # request their info
        PostalCode.zip_write_to_file(user_zip_input)
        zipResponse = PostalCode.make_zip_request(user_zip_input)
        # fileWriter = open("C:/Users/Lope/PycharmProjects/Project3/Seperator/zip_code_response.html", mode="r")
        # fileWriter.write(zipResponse)

        PostalCodeList = PostalCode.read_table_data()
        lastfile = open("C:/users/lope/pycharmProjects/Project3/Seperator/zipList.txt", mode="w+")
        lastfile.write(PostalCodeList.text)

    #         except os.error.errno:
    #                 print("File could not be found. Try and enter your response again")
    #
    #     else:
    #         print("Did not receive a response. Check your connection and try again.")
    #
    # finally:
    #     print("Program has reached the end and will not terminate")
    #     exit(0)
    # # except Exception as ex:
    #     print("Error info " + str(ex))




app = Main()

app


