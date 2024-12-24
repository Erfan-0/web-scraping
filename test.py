import requests  
from bs4 import BeautifulSoup
import time


print('requesting...')
response = requests.get('https://bslife.ir/index.php?post=Lucky')
web_content = response.text
soup = BeautifulSoup(web_content, 'html.parser')

print('esami sherkat konandegan ta iin lahze: ')
time.sleep(2)

name_list = []
shomare = 1
for i in soup.find_all("tr"):  
    tds = i.find_all("td") 
    if len(tds) > 1:
        print(f"{shomare}: {tds[1].text}")
        shomare += 1
        name_list.append(tds[1].text)


print(name_list)


