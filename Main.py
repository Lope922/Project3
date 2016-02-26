import requests
from bs4 import BeautifulSoup




# create request to the floodsafety website , reads response in html5
r = requests.get("http://www.floodsafety.noaa.gov/", "html5lib")


soup = BeautifulSoup(r.content, "html5lib")
#print(soup.prettify())
tables = soup.select("tr")

# and here it is what i want, now to put it into a text box/Form & display what to do.
#print(tables[1])
print(tables[1].find("p"))
info = tables[1].find("p")
str(info)
#print(tables)


#todo strip the hypertext format from phrase
# store this either into a file or a variable to write onto a form.

#todo write to a file
s = open('floodinfo', "a")

s.write(str(info))

#todo read from a file to make the next request using the zip provided through a different program.

zip = 0

# open a file in the given path with the directory open it with the read only privleges.
#f = open('workfile', 'r')



