import requests
import re
import time
import json
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from common.Chromedriver import ChromeDriver
from common.MakeHtml import MakeHtml
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wordprocess():
    def __init__(self)  -> None:
        chromedriver = ChromeDriver()
        chromedriver.Decompress_Chrome_Driver()
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('headless')
        self.options.add_argument('disable-gpu')
        chrome_path = f'{chromedriver.driver_path}\{chromedriver.current_version}\chromedriver-win32\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=chrome_path)
        print()
        # self.driver = webdriver.Chrome(service=Service(executable_path=chrome_path), options=self.options)

    def WriteBlog(self):
        try:
            if self.Login():
                self.driver.get('https://mckimblog.co.kr/wp-admin/post-new.php')
                self.driver.find_element(By.ID, "content-html").click()

                # 제목작성
                title = '테스트'
                self.driver.find_element(By.ID, 'title').send_keys(title)

                # 본문작성
                content = '본문 예시'
                self.driver.find_element(By.ID, 'content').send_keys(content)

                # 포커스 키워드 작성

                # 이미지 추가1
            
        except Exception as e:
            print(e)




    def Login(self):
        result = True
        try:
            url = 'https://mckimblog.co.kr/wp-login.php?redirect_to=https%3A%2F%2Fmckimblog.co.kr%2Fwp-admin%2F&reauth=1'
            self.driver.get(url)
            time.sleep(5)

            id_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "user_login"))
            )
            id_element.send_keys("아이디")
            time.sleep(2.5)

            pw_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "user_pass"))
            )
            pw_element.send_keys("패스워드")
            time.sleep(2.5)

            self.driver.find_element(By.ID, "wp-submit").click()
            time.sleep(10)
        except Exception as e:
            result = False
            print(f'로그인 실패  ::  {e}')

        return result