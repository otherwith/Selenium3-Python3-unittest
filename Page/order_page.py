from selenium.webdriver.common.by import By
from Base.base import Base
import time

class OrderPage(Base):
    """订单界面"""
    def __init__(self,browser):
        self.browser = browser

    def detail_name(self):
        """
        乘客姓名输入框
        :return:
        """
        return self.findele(By.XPATH,"//*[@id='pasglistdiv']/div/ul/li[2]/input")

    def user_info(self,username):
        """
        填写用户名
        :return:
        """
        self.detail_name().send_keys(username)