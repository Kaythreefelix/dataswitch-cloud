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

class HomePageDashboard(unittest.TestCase):
    @classmethod
    def test_setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_home_page_dashboard(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("https://dataswitch.k3imagine.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("name").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Testing552!")
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-k3").click()
        time.sleep(2)

        # wait = WebDriverWait(driver, 10)
        # try:
        #     element = wait.until(EC.element_to_be_clickble((By.XPATH, ".//*[normalize-space(text()) and normalize-space(.)='Terms & Conditions'])[1]/following::button[1]")))
        #     print("element is clickable")
        # except:
        #     print("element is not clickable")
        #     exit(1)
        #
        # element.click()

        #self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Terms & Conditions'])[1]/following::button[1]").click()

       ###### self.driver.find_element_by_css_selector("body > app-dashboard > div.container-fluid.login-screen > div > div.col-md-9.col-lg-6.h-100.login-holder.d-flex.align-items-center.animated.slideInLeft > form > button").click()
        self.driver.close()

        # self.driver.find_element_by_id("name").clear()
        # self.driver.find_element_by_id("name").send_keys("admin")
        # self.driver.find_element_by_id("password").clear()
        # self.driver.find_element_by_id("password").send_keys("Testing552!")
        # self.driver.find_element_by_id("name").click()
        # self.driver.find_element_by_id("name").click()
        # self.driver.find_element_by_xpath("//form").click()
        # self.driver.find_element_by_id("password").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Terms & Conditions'])[1]/following::button[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Dashboard'])[1]/following::a[4]").click()
        # self.driver.find_element_by_link_text("| Insights").click()
        # self.driver.find_element_by_link_text("| Configuration").click()
        # self.driver.find_element_by_link_text("| Administration").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Last Logged In : Oct 14, 2019 - 7:59 AM'])[1]/following::button[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select a Project'])[2]/following::span[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select a Project'])[2]/following::span[1]").click()
        # self.driver.find_element_by_link_text("Aaron Wilcock").click()
        # self.driver.find_element_by_link_text("Profile").click()
        # self.driver.find_element_by_link_text("Aaron Wilcock").click()
        # self.driver.find_element_by_link_text("Logout").click()
        # self.driver.find_element_by_id("name").clear()
        # self.driver.find_element_by_id("name").send_keys("admin")
        # self.driver.find_element_by_id("password").clear()
        # self.driver.find_element_by_id("password").send_keys("Testing552!")
        # #driver.close()

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
        #self.assertEqual([], self.verificationErrors)
        print('TEST COMPLETE')

if __name__ == "__main__":
    unittest.main(verbosity=2)
