import time
from selenium import webdriver
import sys



mobile_emulation = { "deviceName": "Nexus 5" }

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

discordMailboxName= "email"
discordUserboxName = "username"
dicordPasswordBoxName = "password"
BornYear = "react-select-2-input"
BornMonth = "react-select-3-input"
BornDay = "react-select-4-input"
driver = webdriver.Chrome(executable_path='./chromedriver.exe',desired_capabilities=chrome_options.to_capabilities())

def WriteForm(Email,Username,Password,Bornyear,Bornmonth,Bornday):
    
    driver.get('https://discord.com/register')
    Mailbox = driver.find_element_by_name("email")
    Mailbox.send_keys(Email)

    UserName = driver.find_element_by_name(discordUserboxName)
    UserName.send_keys(Username)


    UserPassword = driver.find_element_by_name(dicordPasswordBoxName)
    UserPassword.send_keys(Password)

    BornYearC = driver.find_element_by_id(BornYear)
    BornYearC.send_keys(Bornyear)

    BornMonthC = driver.find_element_by_id(BornMonth)
    BornMonthC.send_keys(Bornmonth)

    BornDayC = driver.find_element_by_id(BornDay)
    BornDayC.send_keys(Bornday)
    try:
        driver.find_elements_by_tag_name("input")[6].click()
    except:
        pass
    BornDayC.submit()
    while True:
        time.sleep(5)
        if(driver.current_url == "https://discord.com/channels/@me"):
            time.sleep(10)
            print(driver.execute_script("return window.localStorage.length;"))
    

if __name__ == '__main__':
    sys.exit()
    