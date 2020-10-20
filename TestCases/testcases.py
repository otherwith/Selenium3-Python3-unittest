import time
import unittest
from Base.base import Base
from Page.search_page import SearchPage
from Common.funcation import config_url


class TestDemo(unittest.TestCase):

    def setUp(self):
        Base.browser().get(config_url())
        Base.browser().maximize_window()
        Base.browser().implicitly_wait(10)
        self.searchPage = SearchPage()

    def test_booking_ticket_01(self):
        # 预定火车票->正例（即一切都是正常输入）
        self.searchPage.search_train("西安", "重庆", "2020-10-24")

    # def test_booking_ticket_02(self):
    #     """
    #     预定火车票->反例（即验证非正常或者无效的输入）
    #     :return:
    #     """
    #     self.browser.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")
    #     self.browser.maximize_window()
    #     self.assertEqual(self.browser.find_element(By.XPATH, "//*[@class='s_box_tab']/a[1]").text, "国内火车票",
    #                      "火车票查询页面未正确打开")
    #     self.browser.find_element(By.XPATH, "//*[@id='notice01']").send_keys("西安01")
    #     time.sleep(2)
    #     self.assertEqual(self.browser.find_element(By.XPATH, "//*[@id='mainbody']/div[7]").text, "对不起,找不到：西安01",
    #                      "提示信息错误")

    def tearDown(self):
        Base.browser().quit()


if __name__ == '__main__':
    unittest.main()
