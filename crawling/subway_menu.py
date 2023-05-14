from bs4 import BeautifulSoup

import requests

res = requests.get('https://www.subway.co.kr/?mobile')
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
menu = soup.find_all('div', 'tab')
name = soup.find_all('strong', 'title')

print(len(menu))
menu.splitlines(True)
# print(len(menu))

# for i in range(len(name)):
#     if i == 0:
#         print(menu[0].get_text())
#     elif i == 6:
#         print("-----------------")
#         print(menu[1].get_text())
#     elif i == 10:
#         print("-----------------")
#         print(menu[2].get_text())
#     elif i == 16:
#         print("-----------------")
#         print(menu[3].get_text())
#     print("-", name[i].get_text())
