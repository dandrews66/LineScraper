from bs4 import BeautifulSoup
import requests

def getHTMLData():
    url = 'http://www.sportsbookreview.com/betting-odds/nfl-football/merged/?date=20150913'
    httpResponse = requests.get(url)
    soupHTML = BeautifulSoup(httpResponse.text, 'html.parser')
    gamesArray = soupHTML.find_all('div', class_='event-holder')
    test = 1


def main():
    rawData = getHTMLData()


if __name__ == "__main__":
    main()
