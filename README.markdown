[![Build Status](https://travis-ci.org/testingbot/testingbot_pyunit.svg?branch=master)](https://travis-ci.org/testingbot/testingbot_pyunit)

## TestingBot - Python & PyUnit

TestingBot provides an online grid of browsers and mobile devices to run Automated tests on via Selenium WebDriver.
This example demonstrates how to use Python with PyUnit to run tests across several browsers.

### Environment Setup

1. TestingBot Credentials
    * Add your TestingBot Key and Secret as environmental variables. You can find these in the [TestingBot Dashboard](https://testingbot.com/members/).
    ```
    $ export TESTINGBOT_KEY=<your TestingBot Key>
    $ export TESTINGBOT_SECRET=<your TestingBot Secret>
    ```

### Running Tests

* Sample Test:
    ```
    $ python test/test.py
    ```
You will see the test result in the [TestingBot Dashboard](https://testingbot.com/members/)

### Resources
##### [TestingBot Documentation](https://testingbot.com/support/)

##### [SeleniumHQ Documentation](http://www.seleniumhq.org/docs/)

##### [PyUnit Documentation](https://docs.python.org/3/library/unittest.html)
