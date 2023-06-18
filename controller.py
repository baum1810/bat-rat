import requests
from os import system

apilink = "YOURAPILINKHERE"


def main():
    system("cls")
    cmd = input("cmd\n> ")
    r = requests.post(f"{apilink}/setcommand",data={'cmd':cmd})

    
while True:
    try:
        main()
    except:
        main()
