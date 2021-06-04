import selenium
import sys
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

with open('login.json') as json_file:
    login_data = json.load(json_file)

driver = webdriver.Chrome()

#server switch
if(sys.argv[2] == 1):
    driver.get('https://neptun11.uni-pannon.hu/hallgato/login.aspx')
elif(sys.argv[2] == 2):
    driver.get('https://neptun12.uni-pannon.hu/hallgato/login.aspx')
elif(sys.argv[2] == 3):
    driver.get('https://neptun13.uni-pannon.hu/hallgato/login.aspx')

#login page elements
neptun_code = driver.find_element_by_name('user')
password = driver.find_element_by_name('pwd')
login_button = driver.find_element_by_name('btnSubmit')

#login credentials from json
neptun_code.send_keys(login_data['neptun_code'])
password.send_keys(login_data['password'])

login_button.click()

timeout = 10
try:
    element_present = EC.presence_of_element_located((By.NAME, 'upSystemParams$upmodalSystemParams$upFootermodalSystemParams$footerbtn_modalSystemParams_Vissza'))
    WebDriverWait(driver, timeout).until(element_present)
    back_button = driver.find_element_by_name('upSystemParams$upmodalSystemParams$upFootermodalSystemParams$footerbtn_modalSystemParams_Vissza')
    back_button.click()
except TimeoutException:
    print("///FATAL EXCEPTION: PAGE LOADING TIMEOUT///")

if(sys.argv[1] == 'órarend'):
    studies_button = driver.find_element_by_id('mb1_Tanulmanyok')
    studies_button.click()

    timetable_button = driver.find_element_by_id('mb1_Tanulmanyok_Órarend')
    timetable_button.click()
elif(sys.argv[1] == 'leckekönyv'):
    studies_button = driver.find_element_by_id('mb1_Tanulmanyok')
    studies_button.click()

    timetable_button = driver.find_element_by_id('mb1_Tanulmanyok_Leckekonyv')
    timetable_button.click()
elif(sys.argv[1] == 'tárgyfelvétel'):
    timetable_button = driver.find_element_by_id('mb1_Targyak')
    timetable_button.click()

    timetable_button = driver.find_element_by_id('mb1_Targyak_Targyfelvetel')
    timetable_button.click()