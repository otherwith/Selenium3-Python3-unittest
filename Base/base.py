from selenium import webdriver


class Base():
    driver = None

    def __init__(self):
        pass

    @classmethod
    def browser(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
        return cls.driver

    def findele(self, *locator):
        """
        定位元素
        :param loactor:
        :return:
        """
        return self.browser.find_element(*locator)

    def click(self, *loactor):
        """
        对元素进行点击操作
        :param loactor:
        :return:
        """
        self.findele(*loactor).click()

    def sendkeys(self, *loactor, value):
        """
        输入值
        :param loactor:
        :return:
        """
        self.findele(*loactor).send_keys(value)

    def execute_js(self, str):
        """
        执行js
        :param str:
        :return:
        """
        self.browser.execute_script(str)

    def url(self):
        """
        获取网址
        :return:
        """
        return self.browser.current_url

    def back(self):
        """
        后退
        :return:
        """
        self.browser.back()

    def forword(self):
        """
        前进
        :return:
        """
        self.browser.forward()

    def quit(self):
        """
        退出浏览器
        :return:
        """
        self.browser.quit()

    def open(self, url):
        """
        打开网址
        :return: 
        """
        self.browser.get(url)
