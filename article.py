from selenium import webdriver
from selenium.webdriver.support.select import Select


browser = webdriver.Firefox()

browser.get('http://apps.webofknowledge.com.prox.lib.ncsu.edu/')
assert 'Home Organization Selection' in browser.title

selection = browser.find_element_by_name('user_idp')
for option in selection.find_elements_by_tag_name('option'):
    if option.text == 'NC State Unity Users':
        option.click()
        break

submit = browser.find_element_by_name('Select')
submit.click()
#browser.quit()
