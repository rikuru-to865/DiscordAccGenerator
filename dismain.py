import Getmail
import DAC as DiscordForm
import random, string
import time
import threading

mail = Getmail.getMail()

        


def randomstring(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)



DiscordForm.WriteForm(mail,randomstring(5),randomstring(7),random.randrange(1980,2000),random.randrange(1,12),random.randrange(1,30))
