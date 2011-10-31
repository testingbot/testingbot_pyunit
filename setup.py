from setuptools import setup, find_packages
setup(name='Testingbot',
      version = "0.0.2",
      author = "Testingbot",
      author_email = "info@testingbot.com",
      description = "Python selenium package to be used with TestingBot.com's Selenium Grid",
      url = "http://www.testingbot.com",
      packages=find_packages(),
      install_requires= ['pyunit', 'selenium'],
      entry_points={
        'console_scripts': [
           'testingbot = testingbot.install:install' ]
      }
)