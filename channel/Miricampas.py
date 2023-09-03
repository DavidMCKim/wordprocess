import requests
import re
import time
import json
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.Chromedriver import ChromeDriver
from common.MakeHtml import MakeHtml
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Miricampas():
    def __inti__() -> None:
        print()
    
    def miricampas():
        print()

    def Login(self):
        result = True
        try:
            url = 'https://www.miricanvas.com/ko'
            self.driver.get(url)
            time.sleep(5)

            id_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "headerBtnSignIn"))
            )
            id_element.click()

            self.driver.find_element(By.ID,'loginPopup').find_elements(By.CLASS_NAME,'KoSocialSignSelectBoxView__Logo-sc-e23ab5c5-4')[2].click()


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