import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User Agents": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}

for count in range(1, 8):
    sleep(3)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all("div", class_ = "w-full rounded border")

    for i in data:
        url_img = "https://scrapingclub.com" + i.find("img").get("src")

        name = i.find("h4").text.replace("\n", "")

        price = i.find("h5").text.replace("\n", "")

        print(url_img, name, price)