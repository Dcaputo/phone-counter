# counter
import time
import webbrowser
import selenium
from selenium import webdriver

#what number you are searching
number = input('enter number: ')
url = f'https://www.advancedbackgroundchecks.com/{number}'+'{}'

driver = webdriver.Chrome()
for count in range(100):
    webbrowser.open(url.format('{0:02d}'.format(count)))
