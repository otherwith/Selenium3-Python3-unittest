from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
class TestDemo(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)


    def test_booking_ticket_01(self):
        #预定火车票->正例（即一切都是正常输入）
        
        self.browser.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")
        self.browser.maximize_window()
        self.assertEqual(self.browser.find_element(By.XPATH,"//*[@class='s_box_tab']/a[1]").text,"国内火车票","火车票查询页面未正确打开")
        self.browser.find_element(By.XPATH,"//*[@id='notice01']").send_keys("西安")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//*[@id='notice08']").send_keys("成都")
        time.sleep(2)
        self.browser.execute_script("document.querySelector('#dateObj').removeAttribute('readonly')")
        self.browser.find_element(By.XPATH, "//*[@id='dateObj']").clear()
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//*[@id='dateObj']").send_keys("2020-02-10")
        ActionChains(self.browser).move_by_offset(0,0).click().perform()
        self.browser.find_element(By.XPATH,"//*[@id='searchbtn']").click()
        time.sleep(3)
        self.assertEqual(self.browser.find_element(By.XPATH,"//*[@class='trainList_title']/h2/strong[1]").text,"西安","出发站信息填写不正确")
        self.assertEqual(self.browser.find_element(By.XPATH, "//*[@class='trainList_title']/h2/strong[2]").text, "成都",
                         "出发站信息填写不正确")
        self.assertEqual(self.browser.find_element(By.XPATH,"//*[@id='dateObj']").get_attribute("value"),"2020-02-10","出发时间填写不正确")
        self.browser.find_element(By.XPATH,"//*[@id='tbody-01-G8911']/div[1]/div[6]/div[1]/a").click()
        time.sleep(3)
        self.assertEqual(self.browser.find_element(By.XPATH,"//*[@id='aspnetForm']/div[4]/div[1]/div[3]/h2").is_displayed(),True,"乘客信息填写页面展示错误")
        self.browser.find_element(By.XPATH,"//*[@id='pasglistdiv']/div/ul/li[2]/input").send_keys("Aiyouz")
        time.sleep(5)


    def test_booking_ticket_02(self):
        """
        预定火车票->反例（即验证非正常或者无效的输入）
        :return:
        """
        self.browser.get("https://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")
        self.browser.maximize_window()
        self.assertEqual(self.browser.find_element(By.XPATH,"//*[@class='s_box_tab']/a[1]").text,"国内火车票","火车票查询页面未正确打开")
        self.browser.find_element(By.XPATH,"//*[@id='notice01']").send_keys("西安01")
        time.sleep(2)
        self.assertEqual(self.browser.find_element(By.XPATH,"//*[@id='mainbody']/div[7]").text,"对不起,找不到：西安01","提示信息错误")

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
