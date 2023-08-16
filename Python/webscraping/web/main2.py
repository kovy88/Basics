from bs4 import BeautifulSoup

with open("info.html") as info:
    html = info.read()

soup = BeautifulSoup(html, "html.parser")
# heading = soup.h1
# heading2 = soup.h2
# history_list = soup.ul
# all_p = soup.findAll("p")
# print(heading)
# print(heading2)
# print(history_list)
# print(all_p)
# print(all_p[0])
# print(all_p[1])
# for i in all_p:
#     print(i)
# for i in all_p:
#     print(i.getText())
#
# all_a = soup.findAll("a")
# print(all_a)
# for i in all_a:
#     print(i)
# for i in all_a:
#     print(i.getText())
# for i in all_a:
#     print(i.get("href"))

x = soup.find(class_="company-name")
y = soup.find(id="history-list")
print(y)
