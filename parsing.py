import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User Agents": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}

def get_url():
    for count in range(1, 8):

        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_ = "w-full rounded border")

        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url
        
urls = get_url()

def array():      
    for card_url in urls:
        
        response = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("div", class_ = "my-8 w-full rounded border")
        
        card_img = "https://scrapingclub.com" + data.find("img").get("src")
        card_title = data.find("h3").text
        card_price = data.find("h4", class_="my-4 card-price").text
        card_discription = data.find("p", class_="card-description").text
        
        yield card_title, card_price, card_discription, card_img
        
array = array()