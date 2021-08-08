from bs4 import BeautifulSoup
import urllib.request as req

# 서버한테 요청 메시지 보내고, HTML 코드 받기
code=req.urlopen("http://www.cgv.co.kr/movies/")
# print(code.read())

#HTML 코드 이쁘게 정리하기
soup=BeautifulSoup(code,"html.parser")
#print(soup)
#내가 원하는 요소를 컴퓨터한테 설명하기

title=soup.select("strong.title")


# 요소 내용 출력하기
#print(title)

for i in title:
    print(i.string)