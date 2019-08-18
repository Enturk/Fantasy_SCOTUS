# Fantasy_SCOTUS
Python project scraping web results and using the Google API to manage [a Fantasy SCOTUS League](https://cgttsc.wordpress.com/2015/10/14/citizens-guide-scotus-fantasy-league-rules-and-disclosures/). The [Citizen's Guide to the Supreme Court](https://cgttsc.wordpress.com/) has run a ramshackle contest every Supreme Court term for the past couple of years, where listeners compete to try to be the one who guesses the most points worth of correctness. Guessing which party gets the better end of things is 15 points, guessing how many justices vote for the majority gets 25 points, and guessing the majority author gets you 30 points, over a handful of cases selected by the hosts each month. Ballots are collected via a google form which were, for now, put into spreadsheets to calculate winners. 

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
* The right way to scrape a website. Beautiful soup used to be it, but now there's [Mechanize](https://github.com/sparklemotion/mechanize), [MechanicalSoup](https://github.com/MechanicalSoup/MechanicalSoup), and [Scrapy](https://scrapy.org/). On top of this, there are ethical concerns that I'm not sure how to negotiate. Oyez.com, for example, seems to respond to all my scraping attempts with an invitation to use a better browser. I'm guessing this is a way to dissuade me from scraping it, so I'm focusing on scotusblog. But maybe I could figure this out from a site's [robots.txt and other details](https://medium.com/velotio-perspectives/web-scraping-introduction-best-practices-caveats-9cbf4acc8d0f). Or maybe [making Requests a bit more polite, like this](https://realpython.com/python-web-scraping-practical-introduction/)?
* The right way to push the information to google sheets. This is more a matter of just [getting it to work](https://stackoverflow.com/questions/47384121/while-working-with-gspread-pandas-module-i-want-to-change-default-dir-of-the-mo), I think. But my very brief initial attempts have been unsuccessful, but I think I've been lazy. I should probably just use the API directly instead of using a library. But, before I try that, I might try [fixing the credentials](https://gspread-pandas.readthedocs.io/en/latest/gspread_pandas.html#module-gspread_pandas.conf) or look into the more popular [Pygsheets](https://erikrood.com/Posts/py_gsheets.html).
* There's the need to build a better interface. At the moment, updating what to keep and discard after scraping is a pain in the arse. Any website will eventually make changes, and it would be nice to log request responses to build an easier way to adapt to those changes. 
* Some natural language processing might be helpful in doing the above, or even at least in determining which party has prevailed for our [fantasy SCOTUS league purposes](https://cgttsc.wordpress.com/2015/10/14/citizens-guide-scotus-fantasy-league-rules-and-disclosures/). This is complicated in many cases, because often the result is an order for the lower court to review the case to make the outcome conform to a (relatively, and often absolutely, complex opinion). I'm eyeballing [SpaCy](https://spacy.io/) for that, but I don't have much of a plan here. I often wonder if I could scrape other sites to just get a sense of who wins based on the reactions to the outcome.
