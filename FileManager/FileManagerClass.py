import os
import shutil

class CustomFileManager:
    def __init__(self):
        # self.path = os.path.curdir
        # file = "filename"
        # dir = os.path.dirname("/ResponseInfo")
        return self
#C:\Users\Lope\PycharmProjects\Project3
an_easy_path = "C:/Users/Lope/PycharmProjects/Project3/Seperator/"

def chk_dir_exists():
    if os.path.isdir(an_easy_path):
            #os.path.exists(relative_path + "/Response_info"):
        print("path does already exist")
    else:
       initialize_directory()

def initialize_directory():

    os.mkdir(an_easy_path)
    print("you may want to find where else seperator directories were made")

# todo don't run cleanup until have made a sucessfull commit in this branch
def run_clean_up():
    try:
        #if os.path.isdir("Response_info"):
        # this will remove the tree and its entire contents [tread carefully here]
        shutil.rmtree(an_easy_path)
        #os.remove("file1")
        #os.remove("file2")
        #os.remove("file3")
    except Exception as noGood:

        print("something bad happened windows cannot find the path specified " + str(noGood)) # see what happens when this error message is thrown to
        #better define this problem.

