import requests
import re
import time
import json
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from common.MakeHtml import MakeHtml
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from common.Chromedriver import ChromeDriver
from selenium.webdriver.common.keys import Keys
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

            self.driver.find_element(By.ID,'loginPopup').find_elements(By.CLASS_NAME,'KoSocialSignSelectBoxView__Logo-sc-e23ab5c5-4')[0].click()

            # 카카오톡 로그인 팝업창으로 창 전환
            self.driver.switch_to_window(self.driver.window_handles[1])
            self.driver.find_element(By.ID,'loginId--1').send_keys("wedaehan96@naver.com")
            self.driver.find_element(By.ID,'password--2').send_keys("Rkswlska96!^^")
            self.driver.find_element(By.ID,'password--2').send_keys(Keys.ENTER)

            self.driver.switch_to_window(self.driver.window_handles[0])
            self.driver.find_element(By.ID,'btnDisAgreeStayLogin').send_keys(Keys.ENTER)

            # 템플릿 클릭
            self.driver.find_elements(By.CLASS_NAME,'WorkspaceAsideMenuBarView__Tab-sc-f1e2e209-2')[1].click()
            self.driver.find_element(By.CLASS_NAME,'template_search_input').send_keys("대출")
            self.driver.find_element(By.CLASS_NAME,'template_search_input').send_keys(Keys.ENTER)

            self.driver.find_elements(By.CLASS_NAME,'template_item_container')[0].click()
            self.driver.find_element(By.CLASS_NAME,'use_template_button').click()

        except Exception as e:
            result = False
            print(f'로그인 실패  ::  {e}')

        return result        