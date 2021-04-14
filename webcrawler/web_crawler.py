#!/usr/bin/env python

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.uzwil.ch/de/kontakt/personenregister/')

elements = browser.find_elements_by_tag_name('a')
print('***Personen***')

for element in elements:
    if 'Peter' in element.text:
        print(element.text)
        print('\n')

