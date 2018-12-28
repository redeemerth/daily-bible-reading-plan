import csv, sys
import urllib.request
from bs4 import BeautifulSoup
from datetime import timedelta, date
import time

########### Build URL #############

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

# Get all of 2016
start_dt = date(2016, 1, 1)
end_dt = date(2016, 12, 31)
i = 1

with open('oneyearbiblepodcast_urls_2016.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Day_Number', 'Reading', 'Title', 'URL', 'Duration_(ms)'])
    for dt in daterange(start_dt, end_dt):
        year = dt.strftime("%Y")
        month = str(dt.strftime("%m")).lstrip("0")
        day = str(dt.strftime("%d")).lstrip("0")
        month_name = str(dt.strftime("%B")).lower()
        weekday_name = str(dt.strftime("%A")).lower()
        # Example URL
        # url = "http://oneyearbiblepodcast.com/daily-bible-reading/2018/12/23/daily-bible-reading-sunday-december-23"
        url = f"http://oneyearbiblepodcast.com/daily-bible-reading/{year}/{month}/{day}/daily-bible-reading-{weekday_name}-{month_name}-{day}"

        print("before")
        print(f"{i}: {url}")

        ########### Get Audio SRC URL from Page #############
        # Get page and the data-url element
        # class="sqs-audio-embed" data-url
        # Example value
        # http://static1.squarespace.com/static/520fcad6e4b0717200274c82/t/5c1acccb2b6a28b3049721e4/1545260290974/OYB_December23_2018_mixdown.mp3/original/OYB_December23_2018_mixdown.mp3
        try:
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'html.parser')
            audio_div = soup.find('div', attrs={'class': 'sqs-audio-embed'})
            bible_passages_div = soup.find('div', attrs={'class': 'sqs-block-content'})
            audio_url = audio_div.attrs['data-url']
            audio_title = audio_div.attrs['data-title']
            audio_duration = audio_div.attrs['data-duration-in-ms']
            bible_passages = bible_passages_div.text

            print("after")
            print(f"{i}: {url}")

            writer.writerow([i, bible_passages, audio_title, audio_url, audio_duration])
        except:
            print("***************************")
            print(f"Problem retrieving page: {url}")
            print("***************************")
            writer.writerow([i, "", "Problem retrieving", url, ""])

        i = i+1
        time.sleep(1)

print("Done executing program")