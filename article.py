from ConfigParser import ConfigParser
from selenium import webdriver
from selenium.webdriver.support.select import Select



# open firefox
browser = webdriver.Firefox()


# go to http://apps.webofknowledge.com.prox.lib.ncsu.edu
browser.get('http://apps.webofknowledge.com.prox.lib.ncsu.edu/')
assert 'Home Organization Selection' in browser.title

# probably reached the point where we tell them we are from ncsu
# selecting Unity User
selection = browser.find_element_by_name('user_idp')
for option in selection.find_elements_by_tag_name('option'):
    if option.text == 'NC State Unity Users':
        option.click()
        break

# clicking on submit button
submit = browser.find_element_by_name('Select')
submit.click()

assert 'NC State University : Shibboleth : Login' in browser.title


# get unity credentials
unity_credentials = ConfigParser()
unity_credentials.read('cred.ini')

username = unity_credentials.get('unityid','username')
password = unity_credentials.get('unityid','password')


# fill in input with credentials
browser.find_element_by_id('j_username').clear()
browser.find_element_by_id('j_username').send_keys(username)
browser.find_element_by_id('j_password').clear()
browser.find_element_by_id('j_password').send_keys(password)
browser.find_element_by_id('formSubmit').click()

#browser.quit()
