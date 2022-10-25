from selenium.webdriver.common.keys import Keys
from core.Base import Base
import time

class Buzzr(Base):

    def __init__(self):
        super().__init__()
        self.site = "http://buzzr.com.br"
    
    def start(self):
        print("INICIANDO BOT NO BUZZR")
        btn = self.findItem(xpath="/html/body/div[2]/div/div[2]/ul/li[2]/a")
        self.click(btn)

    def enviaMSG(self, msg):
        try:
            inputTXT = self.findItem(xpath="/html/body/div[3]/div/div[2]/div[2]/div/div[1]/textarea")
            self.click(inputTXT)
            inputTXT.send_keys(msg)
            inputTXT.send_keys(Keys.ENTER)
        except:
            ...

    def novoChat(self):
        while True:
            try:
                btnNew = self.findItem(xpath="/html/body/div[3]/div/div[2]/div[1]/div/button")
                self.click(btnNew)
                break
            except:
                ...

    def finaliza(self):
        try:
            btnDesligar = self.findItem(xpath="/html/body/div[3]/div/div[2]/div[2]/div/div[3]/button")
            self.click(btnDesligar)
        except:
            ...

b = Buzzr()
b.getHTML(url=b.site)
b.start()
time.sleep(3)
for x in range(b.total):
    b.enviaMSG(msg=b.msg)
    b.finaliza()
    time.sleep(1)
    b.novoChat()
    time.sleep(1)
b.sair()