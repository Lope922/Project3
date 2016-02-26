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

#print(tables)


#todo strip the hypertext format from phrase
# store this either into a file or a variable to write onto a form.