import unittest
import time
#import re
#import HtmlTestRunner
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# # import sys
#sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class IdmTablesModels(unittest.TestCase):
    @classmethod
    def test_setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_idm_tables_models(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("https://dataswitch.k3imagine.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("name").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Testing552!")
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-k3").click()
        time.sleep(2)

      #    self.driver.find_element_by_link_text("Models").click()
      #    self.driver.find_element_by_link_text("IDM Tables").click()
      #
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Test'])[1]/following::div[7]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Test2'])[1]/following::div[5]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Close'])[4]/following::span[1]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='- Test2'])[1]/following::button[1]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='ExchangeRates'])[1]/following::div[5]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='View Data'])[1]/following::div[2]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::button[2]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='ExchangeRates'])[1]/following::div[5]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Reset Deltas'])[1]/following::span[1]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Drop Table?'])[2]/following::button[2]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='IDM Tables'])[2]/following::button[1]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='add IDM Table'])[1]/following::span[1]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Table Name'])[1]/following::div[8]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CloudVid'])[1]/following::div[5]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Edit External Key'])[2]/following::span[1]").click()
      #    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Reset Deltas for table: CloudVid'])[1]/following::span[1]").click()
      # #  self.driver.close()

    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def is_alert_present(self):
    #     try:
    #         self.driver.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally:
    #         self.accept_next_alert = True
    @classmethod
    def test_tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        # self.assertEqual([], self.verificationErrors)
        print('TEST COMPLETE')

if __name__ == "__main__":
    unittest.main(verbosity=2)


# if __name__ == "__main__":
#     unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output='C:/Users/filex.ebiye/PycharmProjects/dsProd_Framework/reports'))
