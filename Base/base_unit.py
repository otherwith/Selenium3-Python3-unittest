import unittest
from Common.funcation import  config_url
from selenium import webdriver

class UnitBase(unittest.TestCase):
    """抽离单元测试中的setUp与tearDown"""
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome()
        cls.browser.get(config_url())
        cls.browser.maximize_window()


    def tearDownClass(cls) -> None:
        cls.browser.quit()