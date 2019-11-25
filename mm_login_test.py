import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GithubWatchRepoTest(unittest.TestCase):

        def setUp(self):
            self.teamname = "csc-510-f19"
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.add_argument("--no-sandbox")
            chromeOptions.add_argument("--disable-setuid-sandbox")
            chromeOptions.add_argument("--disable-dev-shm-using")
            chromeOptions.add_argument("--disable-extensions")
            chromeOptions.add_argument("--disable-gpu")
            chromeOptions.add_argument("start-maximized")
            chromeOptions.add_argument("disable-infobars")
            chromeOptions.add_argument("--headless")
            self.driver = webdriver.Chrome(chrome_options=chromeOptions)
            self.url = "http://34.66.232.72:8065/login"
            self.driver.get(self.url)
            sleep(10)

        def test_login(self):
            self.driver.find_element_by_name('loginId').send_keys("jsdeokar@ncsu.edu")
            self.driver.find_element_by_name('password').send_keys("Jarvisbot@2019")
            self.driver.find_element_by_id('loginButton').click()
            sleep(10)


        def tearDown(self):
            self.driver.close()
