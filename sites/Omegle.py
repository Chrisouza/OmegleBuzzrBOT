from selenium.webdriver.common.keys import Keys
from core.Base import Base
import time

class Omegle(Base):

    def __init__(self):
        super().__init__()
        self.site = "https://www.omegle.com"
    
    def start(self):
        print("INICIANDO BOT NO OMEGLE")
        btn = self.findItem(xpath="/html/body/div[3]/table/tbody/tr[2]/td[2]/img")
        self.click(btn)
        check1 = self.findItem(xpath="/html/body/div[7]/div/p[1]/label/input")
        self.click(check1)
        time.sleep(1)
        check2 = self.findItem(xpath="/html/body/div[7]/div/p[2]/label/input")
        self.click(check2)
        time.sleep(1)
        confirm = self.findItem(xpath="//html/body/div[7]/div/p[3]/input")
        self.click(confirm)

    def enviaMSG(self, msg):
        try:
            inputTXT = self.findItem(xpath="/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea")
            self.click(inputTXT)
            inputTXT.send_keys(msg)
            inputTXT.send_keys(Keys.ENTER)
        except:
            ...

    def novoChat(self):
        while True:
            try:
                btnNew = self.findItem(xpath="/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button")
                self.click(btnNew)
                break
            except:
                ...

    def finaliza(self):
        try:
            btnDesligar = self.findItem(xpath="/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[1]/div/button")
            self.click(btnDesligar)
            time.sleep(1)
            self.click(btnDesligar)
        except:
            ...

o = Omegle()
o.getHTML(url=o.site)
o.start()
time.sleep(3)
for x in range(o.total):
    o.enviaMSG(msg=o.msg)
    o.finaliza()
    time.sleep(1)
    o.novoChat()
    time.sleep(1)
o.sair()