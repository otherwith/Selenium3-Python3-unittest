from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.base import Base

class Page(Base):
    #出发地
    fromstation = (By.XPATH,"//*[@id='notice01']")
    #到达城市
    tostation = (By.XPATH,"//*[@id='notice08']")
    #出发时间
    fromtime = (By.XPATH, "//*[@id='dateObj']")
    #搜索按钮
    searchbtn = (By.XPATH,"//*[@id='searchbtn']")
    #G89,二等座预定按钮
    bookbtn = (By.XPATH,"//*[@id='tbody-01-G8911']/div[1]/div[6]/div[1]/a")
    #乘客信息，姓名输入框
    passengername = (By.XPATH,"//*[@id='pasglistdiv']/div/ul/li[2]/input")

    def __init__(self,browser):
        self.browser = browser

    def fromstation(self):
         return self.findele(By.XPATH,"//*[@id='notice01']")
