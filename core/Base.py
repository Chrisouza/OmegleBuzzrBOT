import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Base:

    def __init__(self):
        settings = self.loadSetting()
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.total = settings['GERAL']['TOTAL']
        self.msg = settings['GERAL']['MSG']

    def loadSetting(self):
        with open("./config.json", "r") as f:
            data = json.load(f)
            return data

    def getHTML(self, url="", query=""):
        self.driver.get(f"{url}/{query}")
        self.driver.implicitly_wait(100)
        return self.driver.page_source

    def findItem(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)
    
    def click(self, btn):
        btn.click()

    def sair(self):
        self.driver.quit()