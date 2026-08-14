import requests
from bs4 import BeautifulSoup
date = input("Which year would you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://web.archive.org/web/20171116101638/http://www.billboard.com/charts/hot-100/{date}"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

song_names = [song.getText() for song in soup.find_all(name="h2", class_="chart-row__song")]

print(song_names)
