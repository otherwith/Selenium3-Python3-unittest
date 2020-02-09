from selenium.webdriver.common.by import By
from Base.base import Base
import time

class SearchPage(Base):
    def __init__(self,browser):
        self.browser = browser

    def search_leave(self):
        """
        出发城市
        :return:
        """
        return self.findele(By.ID,"notice01")

    def search_arrive(self):
        """
        到达城市
        :return:
        """
        return self.findele(By.ID,"notice08")

    def search_date(self):
        """
        出发时间
        :return:
        """
        return self.findele(By.ID,"dateObj")

    def search_btn(self):
        """
        搜索按钮
        :return:
        """
        return self.findele(By.ID,"searchbtn")

    def search_current(self):
        """
        当前所选的车票类型（国内火车票）
        :return:
        """
        return self.findele(By.CSS_SELECTOR,"#searchtype > li.current")

    def search_js(self):
        """
        执行js，去除时间只读属性
        :return:
        """
        jsvalue = "document.querySelector('#dateObj').removeAttribute('readonly')"
        self.execute_js(jsvalue)

    def search_train(self,leave,arrive,leave_date):
        """
        搜索车票
        :param leave: 出发城市
        :param arrive: 到达城市
        :param leave_date: 出发时间
        :return: 当前的url
        """
        self.search_leave().send_keys(leave)
        time.sleep(2)
        self.search_arrive().send_keys(arrive)
        self.search_js()
        self.search_date().clear()
        self.search_date().send_keys(leave)
        self.search_current().click()
        self.search_btn().click()
        time.sleep(3)
        return self.url()