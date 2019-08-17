# main variables
input_dir = ""
input_file = "sources.txt"
if __name__ == "__main__":
    Verbose = True
else:
    Verbose = False

# for folder navigation
import os
script_dir = os.getcwd()
def folder_nav(dir):
    # change to new folder
    if dir == "":
        return script_dir
    elif os.path.exists(os.path.join(script_dir, dir)):
        dir = os.path.join(script_dir, dir)
        if Verbose:
            print(f'Current input directory is {dir}')
    else:
        try:
            if Verbose: print("Input file folder doesn't exist, creating...")
            os.makedirs(script_dir + dir)
            dir = os.path.join(script_dir, dir)
        except Exception as ex:
            print(f'Fatal error - input directory {dir} not found and cannot be created.')
            print(ex)
            quit()
    os.chdir(dir)

# get to scraping
import urllib.request
from bs4 import BeautifulSoup
def get_site_data(url):
    # returns dictionary of headers and paragraphs
    page_dict = {}
    try:
        request = urllib.request.Request(url)
        page = urllib.request.urlopen(request)
        if Verbose: print (page.read().decode('utf-8'))
        soup = BeautifulSoup(page, 'html.parser')
    except Exception as ex:
        print(f'Error - website {url} not reached.')
        print(ex)
        page_dict.update( {'page' : -1} )
        return page_dict
    if Verbose:
        print(soup.prettify())
    # for section in soup.find_all('tr'):
    #
    #     page_dict.update( {section: } )
    return page_dict

def get_pages(file):
    # get url list from input file
    folder_nav(input_dir)
    sites = []
    if Verbose: print(f'Looking for {file} in {os.getcwd()}')
    try:
        with open(input_file) as f:
            for line in f:
                line = line.strip()
                if len(line)>0:
                    sites.append(line)
                return sites
    except Exception as ex:
        print(f'Fatal error - file {file} not found in {input_dir} and cannot be created.')
        print(ex)
        quit()

# main
parser_sites = get_pages(input_file)
for page in parser_sites:
    if Verbose:
        print(f"Working on {page}")
    get_site_data(page)


import re
