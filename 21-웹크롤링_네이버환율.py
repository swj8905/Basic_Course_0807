from bs4 import BeautifulSoup
import urllib.request as req

code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "html.parser")
price = soup.select("ul.data_lst#exchangeList span.value")
f = open("./환율.txt", "w")
for i in price:
    print(i.string)
    f.write(i.string + "\n")
f.close()