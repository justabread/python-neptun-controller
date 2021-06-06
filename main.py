#TODO implement more browsers//add more pages

import sys
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
try:
    if(sys.argv[2] == "1"):
        print("///NEPTUN OPENED ON SERVER 1///")
        driver.get('https://neptun11.uni-pannon.hu/hallgato/login.aspx')
    elif(sys.argv[2] == "2"):
        print("///NEPTUN OPENED ON SERVER 2///")
        driver.get('https://neptun12.uni-pannon.hu/hallgato/login.aspx')
    elif(sys.argv[2] == "3"):
        print("///NEPTUN OPENED ON SERVER 3///")
        driver.get('https://neptun13.uni-pannon.hu/hallgato/login.aspx')
    else:
        print("///FATAL: NOT RECOGNIZED SERVER GIVEN AS PARAMETER///")
except IndexError:
    print("///FATAL: SERVER PARAMETER EMPTY///")

if( not login_data['neptun_code'] or not login_data['neptun_code']):
    print("///FATAL: NEPTUN CODE OR PASSWORD CANNOT BE EMPTY///")
    exit(0)

#login page elements
login_code = driver.find_element_by_name('user')
login_pwd = driver.find_element_by_name('pwd')
login_button = driver.find_element_by_name('btnSubmit')

#login credentials from json
login_code.send_keys(login_data['neptun_code'])
login_pwd.send_keys(login_data['password'])

login_button.click()

timeout = 2
try:
    element_present = EC.presence_of_element_located((By.NAME, 'upSystemParams$upmodalSystemParams$upFootermodalSystemParams$footerbtn_modalSystemParams_Vissza'))
    WebDriverWait(driver, timeout).until(element_present)
    back_button = driver.find_element_by_name('upSystemParams$upmodalSystemParams$upFootermodalSystemParams$footerbtn_modalSystemParams_Vissza')
    back_button.click()
except TimeoutException:
    print("///QUERY POPUP NOT PRESENT///")

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
elif(sys.argv[1] == 'vizsgajelentkezés'):
    timetable_button = driver.find_element_by_id('mb1_Vizsgak')
    timetable_button.click()

    timetable_button = driver.find_element_by_id('mb1_Vizsgak_Vizsgajelentkezes')
    timetable_button.click()
else:
    print("///FATAL: PAGE NOT RECONGIZED///")