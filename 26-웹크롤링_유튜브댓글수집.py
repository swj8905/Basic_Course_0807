from selenium import webdriver
import time
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys

cp = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(cp)
browser.get("https://www.youtube.com/watch?v=95ULYjyiFLQ")
time.sleep(4)

# 첫 댓글 생성시키기
browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN) # PAGE_DOWN : 스크롤을 살짝 내림. / END : 스크롤을 끝까지 내림
time.sleep(5)
comments = browser.find_elements_by_css_selector("#content-text")
idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("----------- 크롤링 끝 --------------")
        break
    idx += 1
    if idx % 20 == 0:
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(5)
        comments = browser.find_elements_by_css_selector("#content-text")