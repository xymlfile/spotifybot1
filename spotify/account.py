import time
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from  lolo import strlist, k
from selenium import webdriver
import random
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
import chromedriver_autoinstaller
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import names
from threading import Thread
from selenium.webdriver.common.action_chains import ActionChains


proxy = "202.91.186.129:8080"
chromedriver_autoinstaller.install()
options = ChromeOptions()
# options.add_argument('--proxy-server=%s' % proxy)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)



def MN():
    for i in range(2):
        driver = webdriver.Chrome(options=options)
        actions = ActionChains(driver)
        driver.get(
            "https://www.spotify.com/en/signup?flow_id=669956d1-ba1e-44f5-a05f-7b949772a67e%3A1711421601&forward_url=https%3A%2F%2Fopen.spotify.com%2F%3Fflow_ctx%3D669956d1-ba1e-44f5-a05f-7b949772a67e%253A1711421601")
        name = names.get_first_name()
        po = str(random.randint(1, 1000000))
        x = random.choice(strlist)
        email = (name + x + po + "@yahoo.com")
        print(email)
        passw = "Beliver123@"

        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.ID, "username").send_keys(email)
        time.sleep(5)
        driver.find_element(By.ID, "username").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element(By.ID, "new-password").send_keys("Beliver123@")
        time.sleep(3)
        driver.find_element(By.ID, "new-password").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element(By.ID, "displayName").send_keys(name)
        driver.find_element(By.ID, "displayName").send_keys(Keys.ENTER)
        actions.send_keys("1992")
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.TAB)
        actions.send_keys("2003")
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.SPACE)
        actions.send_keys(Keys.ENTER)
        time.sleep(2)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(12)
        object = open(r"acts.txt", 'a')
        emailo = (email + "\n")
        object.write(emailo)
        WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#Desktop_LeftSidebar_Id > nav > div > div.hgJel0bLlS_1Uf0EIfSA > div:nth-child(1) > header > div > div > button")))
        # driver.get("https://open.spotify.com/playlist/1qsN7c9SSDlM0jgb7ZXouA")
        # addp = driver.find_element(By.XPATH, """//*[@id="context-menu"]/ul/li[1]/button""")
        # driver.execute_script("arguments[0].click();", addp)
        # time.sleep(5)
        driver.quit()



number_of_threads = 5
threads = []
for number in range(number_of_threads):
        t = Thread(target=MN)
        t.start()
        threads.append(t)
for t in threads:
    t.join()
