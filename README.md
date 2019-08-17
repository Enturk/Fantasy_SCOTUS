# Fantasy_SCOTUS
Python project scraping web results and using the Google API to manage a Fantasy SCOTUS League

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
And Tabulate because I'm lazy:
```
pip3 install tabulate
```
Next, we need to take in the ballots, for which we use the Google Forms API:
```
COMING SOON!
```
Finally, I'm using the Google Sheets API to output the results:
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
