from selenium import selenium
import unittest

import httplib
import urllib
import base64
import sys, traceback, os

def get_testingbot_data():
    file_path = os.path.join(os.path.expanduser('~/'), '.testingbot')
    if not os.path.exists(file_path):
        raise Exception("No .testingbot file found in %s" % file_path)
    f = open(file_path, 'r')
    data = f.read()
    f.close()
    return data.split(":")

def testingbot_stop(self):
    selenium.copy_sessionId = self.sessionId
    selenium._old_stop(self)

selenium._old_stop = selenium.stop
selenium.stop = testingbot_stop

def testingbot_teardown(self):
    etype, value, tb = sys.exc_info()
    success = (etype == None)
    client_key, client_secret = get_testingbot_data()
    params  = urllib.urlencode({'test[success]': success, 'test[status_message]': ''.join(traceback.format_exception(etype, value, tb, 5)).rstrip(),
                                'test[name]': str(self.id().split('.')[-1])})
    conn = httplib.HTTPSConnection("api.testingbot.com")
    base64string = base64.encodestring('%s:%s' % (client_key.rstrip(), client_secret.rstrip()))[:-1].replace("\n", "")
    
    headers = {
        "Content-Type":
        "application/x-www-form-urlencoded; charset=utf-8",
        "Authorization" : "Basic %s" % base64string
    }

    if hasattr(selenium, 'copy_sessionId'):
        sessionId = selenium.copy_sessionId
    else:
        sessionId = self.driver.session_id

    conn.request("PUT", "/v1/tests/%s" % sessionId, params, headers)
    unittest.TestCase._old_method(self)

unittest.TestCase._old_method = unittest.TestCase.tearDown
unittest.TestCase.tearDown = testingbot_teardown