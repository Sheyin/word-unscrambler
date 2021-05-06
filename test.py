import time
from selenium import webdriver

# Optional argument, if not specified will search path.
driver = webdriver.Chrome()
driver.get('http://sheyin.pythonanywhere.com/')
time.sleep(5)  # Let the user actually see something!
letter_box = driver.find_element_by_name('letters')
letter_box.send_keys('stamp')
length_box = driver.find_element_by_name('length')
length_box.send_keys('5')
driver.find_element_by_id("submit").click()

# By now the results page should be showing - search for the intended word
result_div = driver.find_element_by_class_name("results")
# Can maybe look for "Definite words" and "stamp" in results? these are not child elements


time.sleep(5)  # Let the user actually see something!
driver.quit()
