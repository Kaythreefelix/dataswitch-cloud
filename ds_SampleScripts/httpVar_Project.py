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

class HttpProjectTest(unittest.TestCase):
    @classmethod
    def test_setUpClass(cls):
        #global driver
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        # Username_ID = "admin"
        # Password_ID = "Testing552!"
        # Login_XPATH = "(.//*[normalize-space(text()) and normalize-space(.)='Terms & Conditions'])[1]/following::button[1]"

    def test_http_project(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("https://dataswitch.k3imagine.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("name").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Testing552!")
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-k3").click()
        time.sleep(2)


        # self.driver.find_element_by_link_text("Projects").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create a Dataflow'])[21]/following::h5[1]").click()
        # self.driver.find_element_by_link_text("Execute").click()
        # self.driver.find_element_by_id("testButtonIcon").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Var-Test'])[5]/following::div[2]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Var-Test'])[6]/following::div[2]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::button[3]").click()
        self.driver.close()

    # def test_is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def test_is_alert_present(self):
    #     try:
    #         self.driver.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True
    #
    # def test_close_alert_and_get_its_text(self):
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
