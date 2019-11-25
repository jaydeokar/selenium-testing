import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GithubWatchRepoTest(unittest.TestCase):

        def setUp(self):
            self.teamname = "csc-510-f19"
            self.driver = webdriver.PhantomJS()
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
