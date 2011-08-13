import unittest
from selenium import selenium
from testingbot import driver

class testingbot(unittest.TestCase):
    def setUp(self):
        self.browser = selenium(
            'http://hub.testingbot.com',
            4444,
            "*safari",
            'http://www.google.com')
        self.browser.start()
        self.browser.set_timeout(90000)

    def test_sauce(self):
        browser = self.browser
        browser.open("/")
        assert "Google" in browser.get_title()

    def tearDown(self):
        self.browser.stop()
        unittest.TestCase.tearDown(self)

if __name__ == "__main__":
    unittest.main()