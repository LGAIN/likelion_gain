from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.baskinrobbins.co.kr/menu/list.php?top=A')
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
rank = soup.find_all('span', 'ice_name')

for i in range(len(rank)):
    # print(i+1, "위: " + rank[i].get_text())
    # fstring 사용
    print(f'{i+1}위: {rank[i].get_text()}')
