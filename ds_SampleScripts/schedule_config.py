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


class Schedule1Config(unittest.TestCase):
    @classmethod
    def test_setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_schedule1_config(self):
         self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
         self.driver.get("https://dataswitch.k3imagine.com")
         self.driver.maximize_window()
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_id("name").send_keys("admin")
         self.driver.find_element_by_id("password").send_keys("Testing552!")
         time.sleep(2)
         self.driver.find_element_by_class_name("btn-k3").click()
         time.sleep(2)

#          self.driver.find_element_by_link_text("Schedules").click()
#          self.driver.find_element_by_xpath("//div[8]/div/div").click()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Schedules'])[2]/following::button[1]").click()
#          self.driver.find_element_by_id("ijob_name").click()
#          self.driver.find_element_by_id("ijob_name").clear()
#          self.driver.find_element_by_id("ijob_name").send_keys("Test-QA")
#          self.driver.find_element_by_id("project").click()
# #        # self.driver.find_element_by_id("project")).select_by_visible_text("Confirmation_Test_QA")
#          self.driver.find_element_by_id("project").click()
#          self.driver.find_element_by_id("dataflow").click()
#  #       # self.driver.find_element_by_id("dataflow")).select_by_visible_text("Variables-QA")
#          self.driver.find_element_by_id("dataflow").click()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(JSON)'])[1]/following::div[6]").click()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Enabled?'])[1]/following::button[1]").click()
#          self.driver.find_element_by_name("daily").click()
#          self.driver.find_element_by_name("hourRange").click()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='To Hour'])[1]/following::input[1]").click()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='To Hour'])[1]/following::input[1]").clear()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='To Hour'])[1]/following::input[1]").send_keys("0")
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Every (?) Hour'])[1]/following::input[1]").clear()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Every (?) Hour'])[1]/following::input[1]").send_keys("0")
#          self.driver.find_element_by_name("minuteRange").click()
#
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='To Minute'])[1]/following::input[1]").click()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='To Minute'])[1]/following::input[1]").clear()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='To Minute'])[1]/following::input[1]").send_keys("0")
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Every (?) Minute'])[1]/following::input[1]").click()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Every (?) Minute'])[1]/following::input[1]").clear()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Every (?) Minute'])[1]/following::input[1]").send_keys("10")
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Every (?) Second'])[1]/following::button[1]").click()
#          self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'])[1]/following::button[1]").click()
#          self.driver.close()

 #     def test_is_element_present(self, how, what):
 #              try:
 #                 self.driver.find_element(by=how, value=what)
 #              except NoSuchElementException as e:
 #                  return False
 #              return True
 #
 #     def test_is_alert_present(self):
 #              try:
 #                 self.driver.switch_to_alert()
 #              except NoAlertPresentException as e:
 #                  return False
 #              return True
 #
 #     def test_close_alert_and_get_its_text(self):
 #              try:
 #                  alert = self.driver.switch_to_alert()
 #                  alert_text = alert.text
 #                  if self.accept_next_alert:
 #                     alert.accept()
 #                  else:
 #                      alert.dismiss()
 #                return alert_text
 #              finally:
 #                  self.accept_next_alert = True

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
