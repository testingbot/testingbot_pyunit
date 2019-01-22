import unittest
import sys
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from testingbotclient import TestingBotClient

testingbot_key = os.environ.get("TESTINGBOT_KEY")
testingbot_secret = os.environ.get("TESTINGBOT_SECRET")


class Selenium2TestingBot(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = 'latest'
        desired_capabilities['platform'] = 'WINDOWS'
        desired_capabilities['name'] = 'Testing Selenium with Python'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://{}:{}@hub.testingbot.com/wd/hub".format(testingbot_key, testingbot_secret)
        )
        self.driver.implicitly_wait(30)

    def test_google(self):
        self.driver.get('http://www.google.com')
        assert "Google" in self.driver.title

    def tearDown(self):
        self.driver.quit()
        status = sys.exc_info() == (None, None, None)
        tb_client = TestingBotClient(testingbot_key, testingbot_secret)
        tb_client.tests.update_test(self.driver.session_id, self._testMethodName, status)

if __name__ == '__main__':
    unittest.main()