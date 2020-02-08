from selenium import webdriver

class Base():
    def __init__(self,browser=webdriver.Chrome()):
        self.browser = browser

    def findele(self,*loactor):
        """
        定位元素
        :param loactor:
        :return:
        """
        return self.browser.find_element(*loactor)

    def click(self,*loactor):
        """
        对元素进行点击操作
        :param loactor:
        :return:
        """
        self.findele(*loactor).click()

    def sendkeys(self,*loactor,value):
        """
        输入值
        :param loactor:
        :return:
        """
        self.findele(*loactor).send_keys(value)

    def execute_js(self,str):
        """
        执行js
        :param str:
        :return:
        """
        self.browser.execute_script(str)
