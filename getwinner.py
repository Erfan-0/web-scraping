import requests  
from bs4 import BeautifulSoup  

print('requesting...')
response = requests.get('https://ballistica.net/')
web_content = response.text
soup = BeautifulSoup(web_content, 'html.parser') 

account_div = soup.find('div', class_='accountsmall')

if account_div:
    username = account_div.text.strip() 
    print(f"this week's winner: {username}")


    