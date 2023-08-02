# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("http://www.ekospace.cz/")
#
# web = response.text
# soup = BeautifulSoup(web, "html.parser")
# mikro_book = soup.find(class_="ucebnice ucebniceMikro")
# pdf = mikro_book.get("href")
#
# url = "http://www.ekospace.cz/"
# mikro_url = url + pdf
#
# response2 = requests.get(mikro_url)
# with open("mikro.pdf", "wb") as mikro:
#     mikro.write(response2.content)

from bs4 import BeautifulSoup
import requests

res = requests.get("http://www.ekospace.cz/")
url = "http://www.ekospace.cz/"

soup = BeautifulSoup(res.text, "html.parser")

makro_book = soup.find(class_="ucebnice ucebniceMakro")
makro_doc = makro_book.get("href")
result_url = url + makro_doc
result = requests.get(result_url)
with open("makro.doc", "wb") as makro:
    makro.write(result.content)
