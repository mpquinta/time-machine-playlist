import requests
from bs4 import BeautifulSoup

# ask user what date they want to search
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# scrape data for top 100 songs for the given date
URL = f"https://www.billboard.com/charts/hot-100/{date}"

data = requests.get(URL).text

soup = BeautifulSoup(data, "html.parser")

top_song = [soup.find(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet").getText().strip()]


data_song_titles = soup.findAll(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", id="title-of-a-story")

song_titles = top_song + [title.getText().strip() for title in data_song_titles]
print(song_titles)