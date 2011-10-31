import unittest
from selenium import selenium
from testingbot import driver

class testingbot(unittest.TestCase):
    def setUp(self):
        self.browser = selenium(
            'hub.testingbot.com',
            4444,
            "firefox",
            'http://www.google.com')
        self.browser.start('screenrecorder=true;platform=WINDOWS;version=6;screenshot=false')
        self.browser.set_timeout(90000)

    def test_google(self):
        browser = self.browser
        browser.open("/")
        assert "Google" in browser.get_title()

    def tearDown(self):
        self.browser.stop()
        unittest.TestCase.tearDown(self)

if __name__ == "__main__":
    unittest.main()