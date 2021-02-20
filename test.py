import requests


r = requests.get("http://15qm.com/",params={'act':'recv','n':'1011'})
print(r.text)