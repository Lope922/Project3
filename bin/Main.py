import requests
from bs4 import BeautifulSoup
import os.path
import Program.Part1 as Weather
import Program.bin.Part2 as PostalCode



def Main():
    try:
        # request information from National Weather Service
        response = Weather.request_basic_weather_info()

        # if response is not nothing
        if response != None:
            Weather.save_warning_info(response)
            #todo here is where i would like to insert the break/check for call back to retrieve input from other app

            #read zip code file
            try:
                user_zip_input = PostalCode.get_zipcode_response()
                PostalCode.zip_write_to_file(user_zip_input)
                zipResponse = PostalCode.make_zip_request(user_zip_input)

                fileWriter = open("~user\zip_code_response.html", mode="r")
                PostalCodeList = PostalCode.read_table_data(zipResponse,fileWriter)
                fileWriter.write(PostalCodeList)


                relPath = os.path.relpath("/Project3/Program/Response_info/", path="~user")
                print("Here is a relative path " + relPath)


            except os.error.errno:
                    print("File could not be found. Try and enter your response again")

        else:
            print("Did not receive a response. Check your connection and try again.")

    except Exception as ex:
        print("Error info " + str(ex))





app = Main()

app


