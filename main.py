import selenium
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:/Python39/Scripts/chromedriver.exe")

driver.get('https://www.google.hu/?hl=hu')

accept_button = driver.find_element_by_id('L2AGLb')
time.sleep(1) 
accept_button.click()

input_field = driver.find_element_by_name('q')
input_field.send_keys(sys.argv[1])
input_field.send_keys(Keys.RETURN)

first_result = driver.find_elements_by_class_name('g')[0]
first_result.click()