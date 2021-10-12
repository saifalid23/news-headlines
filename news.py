from os import write
from bs4 import BeautifulSoup
import requests

headlinesfile = open('NDTVheadlines.txt',"w")

try:
    source = requests.get('https://www.ndtv.com/')
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text,'html.parser')
    # print(content)
    top_headlines = soup.find('div',class_="cont_cmn top-stories-68")

    all_links = top_headlines.find_all('a',class_='item-title')

    # print(all_links)
    for link in all_links:
        healine = link.text
        print(healine)
        headlinesfile.write("'")
        headlinesfile.write(healine)
        headlinesfile.write("'")
        headlinesfile.write("\n")
        headlinesfile.write("\n")
        
except Exception as e:
    print(e)