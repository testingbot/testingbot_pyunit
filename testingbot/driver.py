from selenium import selenium
import unittest

import httplib
import urllib
import sys, traceback

def testingbot_do_command(self, verb, args):
    conn = httplib.HTTPConnection(self.host, self.port)
    try:
        body = u'cmd=' + urllib.quote_plus(unicode(verb).encode('utf-8'))
        for i in range(len(args)):
            body += '&' + unicode(i+1) + '=' + \
                    urllib.quote_plus(unicode(args[i]).encode('utf-8'))
        if (None != self.sessionId):
            body += "&sessionId=" + unicode(self.sessionId)
        body += "&client_key=7db8dbdf116122fd098b58fd68c2c0f6&client_secret=00da1272195e93e8499f3f799d5797c3"
        headers = {
            "Content-Type":
            "application/x-www-form-urlencoded; charset=utf-8"
        }

        conn.request("POST", "/selenium-server/driver/", body, headers)

        response = conn.getresponse()
        data = unicode(response.read(), "UTF-8")
        if (not data.startswith('OK')):
            raise Exception, data
        return data
    finally:
        conn.close()

def testingbot_stop(self):
    selenium.copy_sessionId = self.sessionId
    selenium._old_stop(self)

selenium._old_stop = selenium.stop
selenium.stop = testingbot_stop

def testingbot_teardown(self):
    etype, value, tb = sys.exc_info()
    success = int(etype == None)
    body = "session_id=" + unicode(self.browser.copy_sessionId) + "&client_key=7db8dbdf116122fd098b58fd68c2c0f6&client_secret=00da1272195e93e8499f3f799d5797c3&status_message=" + ''.join(traceback.format_exception(etype, value, tb, 5)) + "&success=" + str(success) + "&name=" + str(self.id().split('.')[-1]) + "&kind=3"
    conn = httplib.HTTPConnection("api.testingbot.com", 80)
    headers = {
        "Content-Type":
        "application/x-www-form-urlencoded; charset=utf-8"
    }

    conn.request("POST", "/hq/", body, headers)
    unittest.TestCase._old_method(self)

if not hasattr(selenium, '_old_method') :
	selenium._old_method = selenium.do_command
	selenium.do_command = testingbot_do_command

unittest.TestCase._old_method = unittest.TestCase.tearDown
unittest.TestCase.tearDown = testingbot_teardown