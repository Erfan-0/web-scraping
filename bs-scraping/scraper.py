import requests  
from bs4 import BeautifulSoup
import time 


print("""
      
██████╗ ███████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ 
██████╔╝███████╗    ███████╗██║     ██████╔╝███████║██████╔╝██║██╔██╗ ██║██║  ███╗
██╔══██╗╚════██║    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██║██║╚██╗██║██║   ██║
██████╔╝███████║    ███████║╚██████╗██║  ██║██║  ██║██║     ██║██║ ╚████║╚██████╔╝
╚═════╝ ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ 


      
TOOLS:
      
      ballistica [0]

      bslife [1]

""")


tools = int(input('az list bala yek tool ra entekhab konid: ')) 


if tools == 0:
      print("""

      BALLISTICA TOOLS:
            
            namayeshe barande ghore keshi ballistica iin hafte: [0]

            """)
      
      ch_blsta = int(input('yek tool ra entekhab konid: '))

      if ch_blsta == 0:
            print('requesting...')
            response = requests.get('https://ballistica.net/')
            web_content = response.text
            soup = BeautifulSoup(web_content, 'html.parser') 
            account_div = soup.find('div', class_='accountsmall')

            if account_div:
                  username = account_div.text.strip() 
                  print(f"barande iin hafte ghore: {username}")


elif tools == 1:
      print("""

      BSLIFE TOOLS:
                  
            ghore keshi bslife: [0]

            bslife shop: [1]

            ranking etehad haye bslife: [2]

            zamane reset shodane emtiyaz server haye bslife: [3]

            peyda karfane esme khase baraye kharid bslife: [4]

            peyda karfane esme khase baraye kharid bslife: [5]

            """)
      
      ch_bsl = int(input('yek tool ra entekhab konid: '))


      if ch_bsl == 0:

            print("""

            GHORE KESHI TOOLS:

                  namayeshe list tamami sherkat konandegan ta iin lahze: [0]
            
                  peyda kardane esme dar list sherkat konandegan [1]
                  
                  """)
            
            ch_bsl_ghore = int(input('yek tool ra entekhab konid: '))

            name_list = []
            print('requesting...')
            response = requests.get('https://bslife.ir/index.php?post=Lucky')
            web_content = response.text
            soup = BeautifulSoup(web_content, 'html.parser')


            for i in soup.find_all("tr"):  
                  tds = i.find_all("td") 
                  if len(tds) > 1:
                        name_list.append(tds[1].text)            


            if ch_bsl_ghore == 0:
                  print('esami sherkat konandegan ta iin lahze: ')
                  time.sleep(2)

                  shomare = 1
                  for name in name_list:
                        print(f"{shomare}: {name}")
                        shomare += 1
                  

            elif ch_bsl_ghore == 1:
                  try:
                        if not name_list:
                              raise ValueError('kasi dar ghore keshi sherkat nakarde ya file asami sherkat konandegan khali ast!')
                        else:
                              find_name = input('esme ra baraye estelame sherkat dar ghore keshi vared konid: ').lower()
                              if find_name in name_list:
                                    print(f"{find_name} ghablan dar ghore keshi ba movafaghiyat sherkat karde ast")
                              else:
                                    print(f"{find_name} dar ghore keshi sherkat nakarde ast")
                  except ValueError as e:
                        print(f"ERROR: {e}")



    