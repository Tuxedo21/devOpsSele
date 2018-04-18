from selenium import webdriver
from datetime import date
from selenium.webdriver.firefox.options import Options


# Local headless

# options = Options()
# options.set_headless(headless=True)
# browser = webdriver.Firefox( firefox_options=options )

# Remote

browser = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})

browser.get('http://158.85.231.24:10000/IBMEmpleados-1.0-SNAPSHOT/')


today = str(date.today())

# register

nombre = browser.find_element_by_id('nombre')
nombre.send_keys('Theo ' + today)

apPaterno = browser.find_element_by_id('apPaterno')
apPaterno.send_keys('Posthuma ' + today)

apMaterno = browser.find_element_by_id('apMaterno')
apMaterno.send_keys('Solis' + today)

feNacimiento = browser.find_element_by_id('feNacimiento')
feNacimiento.send_keys(today)

registrar = browser.find_element_by_xpath('/html/body/div[1]/form/button[2]')

print "Title: " + browser.title


filename = "selenium_log.txt"

file = open(filename, "w")

if browser.title is not None:
	file.write(browser.title + " :: " + today)	


file.close()

registrar.click()






# clear

