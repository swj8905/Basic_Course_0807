from selenium import webdriver
import time
import chromedriver_autoinstaller
import random

hash_tag = input("해시태그 입력 >> ")

cp = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(cp)
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

id = browser.find_element_by_name("username")
id.send_keys("tutor_pyson") # 본인 아이디 적어주세요.

pw = browser.find_element_by_name("password")
pw.send_keys("q1w2e3r4!@#$")

button = browser.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB")
button.click()
time.sleep(4)
# 해시태그 검색 결과 페이지로 이동
url = "https://www.instagram.com/explore/tags/" + hash_tag
browser.get(url)
time.sleep(5)
# 첫번째 사진 클릭
first_photo = browser.find_element_by_css_selector("div._9AhH0")
first_photo.click()
time.sleep(5)

while True:
    like = browser.find_element_by_css_selector("section.ltpMr.Slqrh svg._8-yf5")
    value = like.get_attribute("aria-label")
    next = browser.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")

    if value == "좋아요":
        like.click()
        time.sleep(random.uniform(30, 40))
        next.click()
        time.sleep(random.uniform(30, 40))
    elif value == "좋아요 취소":
        next.click()
        time.sleep(random.uniform(30, 40))
