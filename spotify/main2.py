from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import WebDriverException
import time
from lolo import acpw, bcacpw, strlist, playlists
from selenium import webdriver
import random
from selenium.webdriver import ChromeOptions
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import names
from threading import Thread
from account import MN


passw = """Beliver123@"""
chromedriver_autoinstaller.install()
options = ChromeOptions()
mobile_emulation = { "deviceName": "Nexus 5" }

options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument("disable-infobars");
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_argument('--headless=new')
# options.page_load_strategy = 'eager'
options.add_experimental_option("useAutomationExtension", False)
options.add_argument('--blink-settings=imagesEnabled=false')
accounts_list = []

while True:
    while True:
        number_of_threads = 2
        threads = []
        for number in range(number_of_threads):
            t = Thread(target=MN)
            t.start()
            threads.append(t)
