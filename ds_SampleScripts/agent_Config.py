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

class AgentsConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_agents_config(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("https://dataswitch.k3imagine.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("name").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("Testing552!")
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-k3").click()
        time.sleep(2)


        # self.driver.find_element_by_link_text("Agents").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create a Location'])[1]/following::div[3]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create a Location'])[1]/following::div[3]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Delete'])[14]/following::div[4]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Delete'])[14]/following::div[4]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Delete'])[17]/following::div[4]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Delete'])[17]/following::div[4]").click()
        #
        # self.driver.find_element_by_link_text("Aaron Wilcock").click()
        # self.driver.find_element_by_link_text("Aaron Wilcock").click()
        #
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Agents & Locations'])[1]/following::input[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Agents & Locations'])[1]/following::input[1]").clear()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Agents & Locations'])[1]/following::input[1]").send_keys("FelixAQ")
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Agents & Locations'])[1]/following::i[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Agents & Locations'])[1]/following::button[2]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Clear'])[1]/following::button[1]").click()
        #
        # self.driver.find_element_by_id("location-name").clear()
        # self.driver.find_element_by_id("location-name").send_keys("AutoAgent")
        #
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[2]/following::button[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create an agent'])[11]/following::button[1]").click()
        #
        # self.driver.find_element_by_id("agent-name").clear()
        # self.driver.find_element_by_id("agent-name").send_keys("Auto_qa")
        #
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Name Your Agent'])[1]/following::i[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create an agent'])[11]/following::div[3]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create an agent'])[12]/following::div[4]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Submit Token'])[1]/following::button[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Agents & Locations'])[1]/following::input[1]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Agents & Locations'])[1]/following::input[1]").clear()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Agents & Locations'])[1]/following::input[1]").send_keys("Auto_qa")
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Agents & Locations'])[1]/following::button[2]").click()
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Manage Agents & Locations'])[1]/following::input[1]").click()
        # self.driver.close()

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
