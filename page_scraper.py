# main variables
input_dir = ""
if __name__ == "__main__":
    Verbose = True
else:
    Verbose = False

# for folder navigation
import os
script_dir = os.getcwd()
def folder_nav(dir):
    if os.path.exists(os.path.join(script_dir, dir)):
        dir = os.path.join(script_dir, dir)
        if Verbose:
            print(f'Current input directory is {dir}')
    else:
        try:
            if Verbose: print("Input file folder doesn't exist, creating...")
            os.makedirs(script_dir + dir)
            dir = os.path.join(script_dir, dir)
        except:
            print(f'Fatal error - input directory {dir} not found and cannot be created.')
            quit()
    os.chdir(dir)

# get to scraping
import urllib2
from bs4 import BeautifulSoup


import sys
import re
