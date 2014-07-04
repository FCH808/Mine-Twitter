### Pulls the 50 US states names and postal code abbreviations from wikipedia.
### Returns dictionary containing a [US State full name: US State Abbreviation] pair for each of the 50 states.


import xml
import urllib
from bs4 import BeautifulSoup

html_page = r"http://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"

def find_all_states():

    soup = BeautifulSoup(urllib.urlopen(html_page))

    table = soup.find('table', class_="wikitable")

    final_dict = {}

    for row in table.find_all('tr')[4:55]:
        all = row.text.encode('utf-8').strip()
        if "State (Commonwealth)" in all:
            full_name, abbrevs = all.split("State (Commonwealth)")
        elif "State" in all:
            full_name, abbrevs = all.split("State")
        elif "Federal district" in all:
            full_name, abbrevs = all.split("Federal district")

        state = full_name.strip()
        abbr = abbrevs[4:6].strip()

        final_dict[state] = abbr

    return final_dict




