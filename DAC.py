import time
from selenium import webdriver
import sys
discordMailboxName= "email"
discordUserboxName = "username"
dicordPasswordBoxName = "password"
BornYear = "react-select-2-input"
BornMonth = "react-select-3-input"
BornDay = "react-select-4-input"
driver = webdriver.Chrome(executable_path='./chromedriver')
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

    BornDayC.submit()

    driver.delete_all_cookies()
if __name__ == '__main__':
    sys.exit()