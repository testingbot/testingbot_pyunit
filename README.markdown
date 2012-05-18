TestingBot.com PyUnit package to use our Selenium Grid.
You can find more info on http://testingbot.com

Install
-------

`easy_install testingbot`

Requirements
------------

You need an API key and API secret from http://www.testingbot.com
You also need to install the selenium and pyunit packages. (easy_install should take care of this for you)

Example (WebDriver)
-------------

    import unittest
    from selenium import webdriver
    from testingbot import driver

    class Selenium2TestingBot(unittest.TestCase):

        def setUp(self):
            desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
            desired_capabilities['version'] = '12'
            desired_capabilities['platform'] = 'WINDOWS'
            desired_capabilities['name'] = 'Testing Selenium 2 in Python'

            self.driver = webdriver.Remote(
                desired_capabilities=desired_capabilities,
                command_executor="http://api_key:api_secret@hub.testingbot.com:4444/wd/hub"
            )
            self.driver.implicitly_wait(30)

        def test_google(self):
            self.driver.get('http://www.google.com')
            assert "Google" in self.driver.title

        def tearDown(self):
            self.driver.quit()
            unittest.TestCase.tearDown(self)

    if __name__ == '__main__':
        unittest.main()


Example (RC)
-------------

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
            self.browser.start('screenrecorder=true;platform=WINDOWS;version=8;screenshot=false')
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
        
Copyright
---------

Copyright (c) 2012 TestingBot.com
See LICENSE for more information.