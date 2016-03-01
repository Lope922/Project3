import os

class CustomFileManager:
    def __init__(self):
        # self.path = os.path.curdir
        # file = "filename"
        # dir = os.path.dirname("/ResponseInfo")
        return self

   # creates the path to save all the temp files created then destroyed.
def initialize_directory():
    #todo fix bug here for differnt environments
    print("program is working out of + " + str(os.path.curdir))
    if os.path.isdir("Response_Info"):
        print("we are good the path to store the response info in is made.")
        open("C:/Users/CaLs_Rig/PycharmProjects/Project3/Program/Response_info/floodinfo.txt", mode="w+")
    else:
        os.mkdir("Response_info")


# this requires program to have access and import os.path. does not work yet. will fix one program is flowing correctly.
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
