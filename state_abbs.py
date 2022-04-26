"""
Download US state abbreviations from SSA
"""

import csv
from bs4 import BeautifulSoup
import urllib

csvfile = "stateabbs.csv"

# SSA site
site = "https://www.ssa.gov/international/coc-docs/states.html"


def getabbs(site):
    # Download source code
    site_text = urllib.request.urlopen(site).read()

    # Parse
    site_soup = BeautifulSoup(site_text)

    # Get data
    site_rows = site_soup.select("table > tr")

    site_rows = [i.getText().strip().split('\n') for i in site_rows]

    site_rows = [[i[0].strip(), i[1].strip()] for i in site_rows]

    site_rows.insert(0, ['State', 'State_Abb'])

    # Save
    with open(csvfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(site_rows)

if __name__ == '__main__':
    getabbs(site = site)



