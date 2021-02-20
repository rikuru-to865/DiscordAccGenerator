import Getmail
import DAC as DiscordForm
import random, string
import time
import threading

mail = Getmail.getMail()

def checkCurrentUrl():
    while True:
        mailURL = Getmail.getMail()
        if DiscordForm.driver.current_url == "https://discord.com/channels/@me":
            Getmail.MailAuthentication(mailURL)
        time.sleep(3)

def randomstring(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)



DiscordForm.WriteForm(mail,randomstring(5),randomstring(7),random.randrange(1980,2000),random.randrange(1,12),random.randrange(1,30))
check = threading.Thread(target=checkCurrentUrl)
check.start()