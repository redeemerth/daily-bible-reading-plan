import csv, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from bs4 import BeautifulSoup
import time

def main(argv):

    url_list = []

    # YouTube URLs
    #url_list.append("https://www.youtube.com/user/jointhebibleproject/videos") # All BP Videos
    url_list.append("https://www.youtube.com/playlist?list=PLH0Szn1yYNeeVFodkI9J_WEATHQCwRZ0u") # OT Playlist
    url_list.append("https://www.youtube.com/playlist?list=PLH0Szn1yYNecanpQqdixWAm3zHdhY2kPR") # NT Playlist

    # CSV Output file name and dir
    output_directory = 'output'
    #csv_name = 'bibleproject_video_metadata.csv'
    csv_name = 'bibleproject_playlist_read-scripture_video_metadata.csv'

    with open(f"{output_directory}/{csv_name}", 'w', newline='') as csvfile:
        # Write header row. Same headers for all YouTube video page types
        writer = csv.writer(csvfile)
        writer.writerow(['TITLE', 'YOUTUBE LABEL', 'VIDEO_ID', 'RETRIEVED_FROM'])
        
        # Get metadata from YouTube
        # A user's /videos and /playlist pages have different structure. Handle separately.
        for url in url_list:
            i = 0
            # Get URL
            browser = webdriver.Chrome('chromedriver')
            browser.get(url)
            html = browser.find_element_by_tag_name('html')
            # Page Down n number of times, e.g. 20
            for i in range(1,20):
                html.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.5)
            # soup has our page
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            browser.quit()
        
            if "/videos" in url:
                for a in soup.findAll('a'):
                    if a.has_attr('id') and a['id'] == 'video-title':
                        i = i + 1
                        video_id = a['href'].split('?v=')[1]
                        title = a['title']
                        youtube_label = a['aria-label']
                        print(f"*title*: {title}, *label*: {youtube_label}, *id*: {video_id}")
                        writer.writerow([title, youtube_label, video_id, "Videos Page"])
            elif "/playlist" in url:
                for div in soup.findAll("ytd-playlist-video-renderer", {"class": "ytd-playlist-video-list-renderer"}):
                    i = i + 1
                    for a in div.findAll("a", {"id": "thumbnail"}):
                        part = a['href'].split('?v=')[1]
                        video_id = part[:part.find('&')]
                    for element in div.findAll("span", {"id": "video-title"}):
                        title = element['title']
                        youtube_label = element['aria-label']
                    print(f"*title*: {title}, *label*: {youtube_label}, *id*: {video_id}")
                    writer.writerow([title, youtube_label, video_id, "Playlist"])

            print(f"Number of videos found: {i}")

    print("Done executing program")

if __name__ == '__main__':
    main(sys.argv[1:])