import requests as rq 
from bs4 import BeautifulSoup as bs 


def getPortInfo(port,url):
    page = rq.get(url)
    soup = bs(page.content,"html.parser")
    table = soup.select("table",class_="wikitable")[4]
    try:
        tr = table.find("td",string=port).parent
        description = tr.find_all("td")[5].text
    except:
        description = "No details about this Port."
    return port,description