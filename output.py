import requests
from os import system
from time import sleep

apilink = "YOURAPILINKHERE"

old = ""

while True:
    r = requests.get(f"{apilink}/getoutput")
    if not r.text == old:
        old = r.text
        system("cls")
        print(r.text)
    
    sleep(1)
