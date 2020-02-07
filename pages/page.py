from selenium import webdriver
from selenium.webdriver.common.by import By

class Page():
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


    def input_fromstation(self,fromstation):
