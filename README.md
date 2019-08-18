# Fantasy_SCOTUS
Python project scraping web results and using the Google API to manage a Fantasy SCOTUS League.

# Warning
This script will not scrape websites that don't want to be scraped. I'm not that guy.

# Requirements
Works with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and the [Google Sheets API](https://developers.google.com/sheets/api/). To get running, you need to install the former. To do this on Linux or Mac systems (with Python 3), use:
```
apt-get install python3-bs4
```

Depending on your situation, you might use:
```
pip3 install beautifulsoup4
```

If you're working on a Mac and get an `urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]`, you need to navigate to `Applications > Python 3.x` and double click on "Install Certificates.command"

Also, this uses [pandas dataframes](https://pandas.pydata.org/) to juggle the data, so if you don't have that:
```
python3 -m pip install --upgrade pandas
```
And Tabulate to make the pretty tables viewable when testing:
```
pip3 install tabulate
```
Now we want to push the results to a spreadsheet. Follow [these instructions to get gspread-pandas working](https://pypi.org/project/gspread-pandas/):
```
pip3 install gspread-pandas
```

# Comments welcome!
This is a spare time project, but I'm looking for ideas about everything, particularly these parts: 
* The right way to scrape a website. Beautiful soup used to be it, but now there's [Mechanize](https://github.com/sparklemotion/mechanize), [MechanicalSoup](https://github.com/MechanicalSoup/MechanicalSoup), and there are ethical concerns that I'm not sure how to negotiate. Oyez.com, for example, seems to respond to all my scraping attempts with an invitation to use a better browser. I'm guessing this is a way to dissuade me from scraping it, so I'm focusing on scotusblog.
* The right way to push the information to google sheets. This is more a matter of just getting it to work, I think. But my very brief initial attempts have been unsuccessful, but I think I've been lazy. I should probably just use the API directly instead of using a library.
* The need to build a better interface. Any website will eventually make changes, and it would be nice to log request responses to build an easier way to adapt to those changes. 
* Some natural language processing might be helpful. I'm eyeballing [SpaCy](https://spacy.io/) for that, but I don't have much of a plan here. 
