"""
Download County Fip Codes from USDA.
The first two elements of the County Fip Code is the state FIP Code.
"""

import csv
import re
# import requests as req
from bs4 import BeautifulSoup
import urllib

csvfile = "countyfips.csv"

# USDA site that contains the fips County Fips
site = 'https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697'


def getfips(site):
    # Download the source code text from the website
    # site_text = req.get(site).text
    site_text = urllib.request.urlopen(site).read()

    # Parse the code
    site_soup = BeautifulSoup(site_text)

    # Get the data (rows in this case)
    site_rows = site_soup.select("div#detail>table>tbody>tr")

    # Create a list to contain the data points
    datalist = []
    for r in site_rows:
        text = r.getText()
        text2 = re.sub(r'\n{1,2}', ',', text)
        text2 = re.sub(r'\s{2,}', ' ', text2)
        text2 = re.sub(r'(^,\s|,\s$)', '', text2)
        datalist.append(text2)

    # Clean data points
    data = [w.split(", ") for w in datalist]

    # Save
    with open(csvfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == "__main__":
    getfips(site=site)
