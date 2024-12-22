import requests  
from bs4 import BeautifulSoup  


print("""
entekhab konid:
      
      ballistica [0]

      bslife [1]

""")



print("""
      
kar haei ke mitoonam najam bedam:
      
      barande ghore keshi ballistica emrooz: [0]

      yaftane esme khod dar list ghore keshi bslife: [1]

      bslife shop: [2]

      ranking etehad haye bslife: [3]

      zamane reset shodane emtiyaz server ha: [4]

      peyda karfane esme khase baraye kharid bslife: [5]

      peyda karfane esme khase baraye kharid bslife: [6]
      
      
      """)
# winnerbls = input(int('')) 

print('requesting...')
response = requests.get('https://ballistica.net/')
web_content = response.text
soup = BeautifulSoup(web_content, 'html.parser') 

account_div = soup.find('div', class_='accountsmall')

if account_div:
    username = account_div.text.strip() 
    print(f"barande emrooz ghore: {username}")


    