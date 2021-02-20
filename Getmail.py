import requests
import time
import attr
from bs4 import  BeautifulSoup
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import DAC


r = requests.session()

def getMail():
    a = r.get("http://15qm.com/",params={'act':'sevin'})
    soup = BeautifulSoup(a.text, "html.parser")
    mail = soup.find("input")
    return mail['value']

def checkMail():
    checkMail = r.get("http://15qm.com/")
    soup = BeautifulSoup(checkMail.text, "html.parser")
    mail = soup.select('td a[href]')
    for tag in mail:
        print(tag.get("href"))
        return tag.get("href")

def MailAuthentication(url):
    DAC.driver.get(url)

if __name__ == '__main__':
    sys.exit()