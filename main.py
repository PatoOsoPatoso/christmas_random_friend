#!/usr/bin/python3

import os
import time
import urllib
import random
import getpasss
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

options = webdriver.ChromeOptions()

if os.name == 'nt':
    user_data_dir = rf'C:\Users\{getpass.getuser()}\AppData\Local\Google\Chrome\User Data'
    user_binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
else:
    user_data_dir = rf'/home/{getpass.getuser()}/.config/google-chrome/Default'
    user_binary_location = r'/usr/bin/google-chrome'

options.add_argument(f'user-data-dir={user_data_dir}')
options.binary_location = user_binary_location

driver = webdriver.Chrome(options=options)

def element_presence(xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def send_message(url):
    driver.get(url)

    element_presence('//*[@id="main"]/footer/div[2]/div/div[5]/div[1]/div[1]/div[2]/div/span', 40)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[2]/div/div[5]/div[1]/div[1]/div[2]/div/span').click()

    element_presence('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]', 40)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys('\n')

    time.sleep(1)

def prepare_msg(name, phone, target):
    base_msg = """Que onda *{}* wachin

Tu amigo invisible es *{}*.

Información importante: https://www.youtube.com/watch?v=iCMfbmU00-g
"""

    base_url = 'https://web.whatsapp.com/send?phone={}&text={}'

    msg = urllib.parse.quote(base_msg.format(name, target))

    url_msg = base_url.format(phone, msg)

    send_message(url_msg)

def main():
    list_numbers = [item.split(':') for item in os.environ.get("PHONE_NUMBERS").split(',')]

    if len(list_numbers) < 3:
        print("There have to be at least 3 numbers in the .env file")
        driver.close()
        exit(1)

    random.shuffle(list_numbers)

    for i in range(len(list_numbers) - 1):
        prepare_msg(list_numbers[i][0], list_numbers[i][1], list_numbers[i+1][0])
    
    prepare_msg(list_numbers[-1][0], list_numbers[-1][1], list_numbers[0][0])

if __name__ == "__main__":
    main()