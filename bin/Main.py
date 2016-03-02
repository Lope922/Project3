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
        thezip = PostalCode.get_zipcode_response()
        # get the zip from the file
        #PostalCode.make_zip_request(thezip)

        # request their info
        zipResponse = PostalCode.make_zip_request(thezip)
        #PostalCode.zip_write_to_file(zipResponse)
        #todo extract the postal code list info
        PostalCode.read_table_data(zipResponse)
        data = ""
        list_of_zip_file_location = open("C:/Users/Lope/PycharmProjects/Project3/Seperator/zipList.txt", mode="w")
        for lin in zipResponse.find_all(name="td", class_="a", attrs="href", recursive=True):

            data += (lin.get_text("href")) + " "
            #print(data)
        list_of_zip_file_location.writelines(data)
        list_of_zip_file_location.close()

        # THIS WORKS , BUT TRYING TO PUT IN ITS PROPER PLACE
        # data = ""
        # list_of_zip_file_location = open("C:/Users/Lope/PycharmProjects/Project3/Seperator/zipList.txt", mode="w")
        # for lin in zipResponse.find_all(name="td", class_="a", attrs="href", recursive=True):
        #
        #     data += (lin.get_text("href")) + " "
        #     print(data)
        # list_of_zip_file_location.writelines((data))
        # list_of_zip_file_location.close()



        # lastfile.write(PostalCodeList.text)
        #PostalCode.writePostal_codes_to_file(PostalCodeList, lastfile)
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


