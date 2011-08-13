import os
import sys

def install():
    api_key = raw_input("Please enter your Testingbot.com API Key: ")
    api_secret = raw_input("Please enter your Testingbot.com API Secret: ")
    write_data(api_key, api_secret)

def write_data(api_key, api_secret):
    path = os.path.expanduser('~/.testingbot')
    f = open(path, 'w')
    f.write(api_key + ":" + api_secret)
    f.close()
    print "You are now ready to use the testingbot.com Selenium grid"

if len(sys.argv) > 1:
    split_data = sys.argv[1].split(':')
    write_data(split_data[0], split_data[1])