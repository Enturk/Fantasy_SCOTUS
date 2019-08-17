# main variables
input_dir = ""
term = 2019
input_file = "sources.txt"
input_file = str(term) + "_" + input_file
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
    except Exception as ex:
        print(f'Fatal error - file {file} not found in {input_dir} and cannot be created.')
        print(ex)
        quit()
    return sites

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
        # print(soup.prettify())
        # print( tabulate(df[0], headers='keys', tablefmt='psql') )
        print(df)
    return df

# for this to work, manage API here:
# https://console.developers.google.com/apis/credentials
from gspread_pandas import Spread, conf
cred = conf.get_config(script_dir, "default.json")
def send_2_sheets(df, sheet):
    # This will ask to authenticate if you haven't done so before
    spread = Spread("fantasyscotus@fantasyscotus.iam.gserviceaccount.com",
                    sheet,
                    config = cred)
    # This will show available sheets:
    if Verbose:
        spread.sheets
    # Save DataFrame to worksheet 'New Test Sheet', create it first if it doesn't exist
    spread.df_to_sheet(df, index=False, sheet=sheet, start='A2', replace=True)
    spread.update_cells('A1', 'A1', ['Created by:', spread.email])
    if Verbose:
        print(spread)

# main
cases = pd.DataFrame(columns = ['Docket No.',
                                'Op. Below',
                                'Argument',
                                'Opinion',
                                'Vote',
                                'Author',
                                'Term'])
parser_sites = get_pages_from_file(input_file)
# during testing, skip first case
first_test_case = Verbose
for page in parser_sites:
    if Verbose:
        print(f"Working on {page}")
    if first_test_case:
        first_test_case = False
    new_case = get_site_data(page)
    if new_case:
        cases = cases.append(new_case, sort=False)
    else:
        print(f'Error - site at {page} did not return a table.')
if Verbose:
    print( tabulate(cases, headers='keys', tablefmt='psql') )
send_2_sheets(cases, str(term) + "_Fantasy_SCOTUS")
