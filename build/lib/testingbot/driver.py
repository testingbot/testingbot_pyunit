from selenium import selenium
import unittest

import httplib
import urllib
import sys, traceback, os

def get_testingbot_data():
    path = os.path.expanduser('~/.testingbot')
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data.split(":")

def testingbot_do_command(self, verb, args):
    conn = httplib.HTTPConnection(self.host, self.port)
    try:
        body = u'cmd=' + urllib.quote_plus(unicode(verb).encode('utf-8'))
        for i in range(len(args)):
            body += '&' + unicode(i+1) + '=' + \
                    urllib.quote_plus(unicode(args[i]).encode('utf-8'))
        if (None != self.sessionId):
            body += "&sessionId=" + unicode(self.sessionId)
        client_key, client_secret = get_testingbot_data()
        body += "&client_key=" + client_key + "&client_secret=" + client_secret
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
    if hasattr(self, 'driver') :
      session_id = self.driver.session_id
    else:
      session_id = self.browser.copy_sessionId
    etype, value, tb = sys.exc_info()
    success = int(etype == None)
    client_key, client_secret = get_testingbot_data()
    body = "session_id=" + unicode(session_id) + "&client_key=" + client_key.rstrip() + "&client_secret=" + client_secret.rstrip() + "&status_message=" + ''.join(traceback.format_exception(etype, value, tb, 5)).rstrip() + "&success=" + str(success) + "&name=" + str(self.id().split('.')[-1]) + "&kind=3"
    conn = httplib.HTTPConnection("testingbot.com", 80)
    headers = {
        "Content-Type":
        "application/x-www-form-urlencoded; charset=utf-8"
    }

    conn.request("POST", "/hq", body, headers)

if not hasattr(selenium, '_old_method') :
    selenium._old_method = selenium.do_command
    selenium.do_command = testingbot_do_command

unittest.TestCase._old_method = unittest.TestCase.tearDown
unittest.TestCase.tearDown = testingbot_teardown