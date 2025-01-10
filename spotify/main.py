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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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


def MN(dr):
    actions = ActionChains( globals()[dr])
    globals()[dr].get(
            "https://www.spotify.com/in-en/signup?flow_id=669956d1-ba1e-44f5-a05f-7b949772a67e%3A1711421601&forward_url=https%3A%2F%2Fopen.spotify.com%2F%3Fflow_ctx%3D669956d1-ba1e-44f5-a05f-7b949772a67e%253A1711421601")
    name = names.get_first_name()
    st = random.choice(strlist)
    po = str(random.randint(1, 10000))
    mo = random.choice(strlist)
    email = (name+st+ mo + po + "@yahoo.com")
    print(email)
    passw = "Beliver123@"
    globals()[dr].minimize_window()
    time.sleep(5)
    globals()[dr].maximize_window()
    time.sleep(5)
    globals()[dr].find_element(By.ID, "username").send_keys(email)
    time.sleep(5)
    globals()[dr].find_element(By.ID, "username").send_keys(Keys.ENTER)
    time.sleep(2)
    globals()[dr].find_element(By.ID, "new-password").send_keys("Beliver123@")
    time.sleep(3)
    globals()[dr].find_element(By.ID, "new-password").send_keys(Keys.ENTER)
    time.sleep(2)
    globals()[dr].find_element(By.ID, "displayName").send_keys(name)
    globals()[dr].find_element(By.ID, "displayName").send_keys(Keys.ENTER)
    actions.send_keys("1992")
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.send_keys(Keys.DOWN)
    actions.send_keys(Keys.ENTER)
    actions.send_keys(Keys.TAB)
    actions.send_keys("23")
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
    time.sleep(50)
ass = []
def bcapwadder():
    with open(r'C:\Users\rudra\Documents\GitHub\spotifybot1\spotify\acts.txt', 'r') as file:
        # Read the lines of the file
        lines = file.readlines()
        for line in lines:
            key = line
            value = passw
            bcacpw[key] = value
bcapwadder()
for i in acpw:
    globals()[f"driver{i}"] = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options= options)



for i in acpw:
    globals()[f"driver{i}"].maximize_window()
    globals()[f"driver{i}"].get("https://accounts.spotify.com/en/login")
    globals()[f"driver{i}"].find_element(By.ID, "login-username").send_keys(i)
    globals()[f"driver{i}"].find_element(By.ID, "login-password").send_keys(passw)
    globals()[(f"driver"
               f"{i}")].find_element(By.ID, "login-password").send_keys(Keys.ENTER)

    time.sleep(5)
    if globals()[f"driver{i}"].current_url == "https://accounts.spotify.com/en/login":
        print(i, "not logged in")
        for b in bcacpw:
            globals()[f"driver{i}"].find_element(By.ID, "login-username").clear()
            globals()[f"driver{i}"].find_element(By.ID, "login-username").send_keys(b)
            globals()[f"driver{i}"].find_element(By.ID, "login-password").clear()
            globals()[f"driver{i}"].find_element(By.ID, "login-password").send_keys(bcacpw[b])
            globals()[f"driver{i}"].find_element(By.ID, "login-password").send_keys(Keys.ENTER)

            time.sleep(5)
            if globals()[f"driver{i}"].current_url == "https://accounts.spotify.com/en/login":
                ass.append(b)

            else:
                bcacpw.pop(b)
                break
        if globals()[f"driver{i}"].current_url == "https://accounts.spotify.com/en/login":
            MN(f"driver{i}")
print(ass)
print( '\033[1m' + 'LOGGING DONE')
print ('\033[0m')

while True:
    for i in acpw:
        playlistlink = random.choice(playlists)
        try:
            globals()[f"driver{i}"].get("https://open.spotify.com/playlist/1WzuaRUxekhPMBZEsszcSe")
            print(1)
            globals()[f"driver{i}"].get(playlistlink)

        except TimeoutError:
            print("t")
        l = False
    print("cycle")
    for i in range(0, 10):
        songsnumberarr = []
        if l == True:
            break

        for i in acpw:
                g = random.randint(1, 6)
                songsnumberarr.append(g)
                try:
                    b = globals()[f"driver{i}"].find_element(By.XPATH,
                                                         f"""//*[@id="main"]/div/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div[{g}]/div/div[1]""")
                    try:
                     globals()[f"driver{i}"].execute_script("arguments[0].click();", b)
                    except WebDriverException:
                        print("element detached")
                    except NoSuchElementException:
                        globals()[f"driver{i}"].get(playlistlink)

                except NoSuchElementException:
                    print("play buttton not found", b)
                    l = True
                    break
                except ElementClickInterceptedException as e:
                    print(e)
                except NoSuchElementException:
                    globals()[f"driver{i}"].get(playlistlink)
                except ElementNotInteractableException:
                    print("play button not interactable")
        print(songsnumberarr)
        time.sleep(10)