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

def get_pages_from_file(file):
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

# get to scraping
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
# fake "real" browser to avoid bad site response
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
def get_site_data(url):
    # returns dictionary of headers and paragraphs
    page_dict = {}
    req = Request(
        url,
        data=None,
        headers=headers
        )
    try:
        page = urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        # TO DO: return -1 if outdated browser response
    except Exception as ex:
        print(f'Error - website {url} not reached.')
        print(ex)
        page_dict.update( {'page' : -1} )
        return page_dict
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    if Verbose:
        print(soup.prettify())
        print( tabulate(df[0], headers='keys', tablefmt='psql') )
    return df

# main
cases = pd.DataFrame()
parser_sites = get_pages_from_file(input_file)
for page in parser_sites:
    if Verbose:
        print(f"Working on {page}")
    cases = pd.concat(cases, get_site_data(page))
print(cases)
