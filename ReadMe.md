# County Fips

## Introduction

This module simply downloads the County Fip Codes from USDA, and saves them as a CSV file in your working directory ("./countyfips.csv"). The name (and path) of the resulting file can be changed in the `csvfile` field in the 4th line of the code.

I created this repo mostly for myself to avoid duplicating the work.

## Dependencies
- `csv` (part of the standard library).
- `re` (part of the standard library).
- `urllib` (part of the standard library). Alternatively, the `requests` library.
- `bs4` (parser).

