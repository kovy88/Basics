from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.seznam.cz/")
soup = BeautifulSoup(response.text, "html.parser")


all_headings = soup.findAll(class_="article__title")


with open("seznam.txt","w") as file:
    for i in all_headings:
        one_article_text = i.getText()
        one_article_link = i.get("href")
        if "Pavel" in one_article_text or "MS" in one_article_text:

            file.write(f"{one_article_text}\n {one_article_link}\n\n")
