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


class Users2Admin(unittest.TestCase):
    @classmethod
    def test_setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_users2_admin(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("https://dataswitch.k3imagine.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("name").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Testing552!")
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-k3").click()
        time.sleep(2)

        self.driver.find_element_by_link_text("Users").click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Loading...'])[1]/following::div[8]").click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Users'])[1]/following::button[1]").click()
        self.driver.find_element_by_id("userName").click()
        self.driver.find_element_by_id("userName").clear()
        self.driver.find_element_by_id("userName").send_keys("EbyFel")
        self.driver.find_element_by_id("email").click()
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys("felix.ebiye@k3btg.com")
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@'])[1]/following::input[2]").click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@'])[1]/following::input[2]").clear()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@'])[1]/following::input[2]").send_keys("Eabee")
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@'])[1]/following::input[3]").click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@'])[1]/following::input[3]").clear()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@'])[1]/following::input[3]").send_keys("Ebbe")
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@'])[1]/following::input[4]").click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@'])[1]/following::input[4]").clear()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='@'])[1]/following::input[4]").send_keys("01617777777")
        self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()


        #driver.close()

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
#     unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output='C:/Users/filex.ebiye/PycharmProjects/dataswitch-cloud/reports'))
