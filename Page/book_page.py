from selenium.webdriver.common.by import By
from Base.base import Base
import time

class BookPage(Base):
    """预定车票界面"""
    def __init__(self,browser):
        self.browser = browser

    def book(self):
        """
        G89列车二等座预定按钮
        :return:
        """
        return self.findele(By.XPATH,"//*[starts-with(@id,'tbody-01-G89')]/div[1]/div[6]/div[1]/a")

    def book_typeG(self):
        """
        车型——G/C高铁勾选框
        :return:
        """
        return self.findele(By.XPATH,"//span[text()='G/C高铁']/../i")

    def book_ticket(self):
        """
        预定车票动作
        :return:
        """
        if self.book_typeG().is_selected() == False:
            self.book_typeG().click()

        time.sleep(2)
        self.book().click()