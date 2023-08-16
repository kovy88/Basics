from bs4 import BeautifulSoup

with open("index.html") as file:
     html_code = file.read()

soup = BeautifulSoup(html_code, "html.parser")

heading = soup.find(id="name")
heading2 = soup.find(class_="about")
print(heading2)

