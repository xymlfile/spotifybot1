import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
import chromedriver_autoinstaller
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager








gl = GoLogin({
 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NzVkZjc5YzA0YTNlMDY2NWViZGUxNjciLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NzVkZjdjNGIwMWNkNjMzMDk3MjI5MWUifQ.7woNwWp1hWyoujl5K9lL1W5JZlOYRje_WysPJdNyKWY',
 'profile_id': '675df79c04a3e0665ebde1ca',
})




debugger_address = gl.start()
options = ChromeOptions()

options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(ChromeDriverManager())
driver.get("127.0.0.1")
time.sleep(100)
# driver.get("https://accounts.spotify.com/en/login")
# driver.find_element(By.ID, "login-username").send_keys("SheliaTYU605130@yahoo.com")
# driver.find_element(By.ID, "login-password").send_keys("Beliver123@")
# driver.find_element(By.ID, "login-password").send_keys(Keys.ENTER)