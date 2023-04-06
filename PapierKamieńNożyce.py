import random
import sys
import time

def main():
    while True:
        choice()

def choice():
    player = input("Papier(p) Kamień(k) Nożyce(n)")
    computer = random.choice(["p","k","n"])
    if(player != "p" and player != "k" and player != "n"):
        sys.exit()
    cchoice = ""
    if(computer == "p"):
        cchoice = "papier"
    elif(computer == "k"):
        cchoice = "kamień"
    else:
        cchoice = "nożyce"
    time.sleep(1.5)
    worl = ""
    if((player == "p" and computer == "k") or (player == "k" and computer == "n") or (player == "n" and computer == "p" )):
        worl = "Wygrałeś"
    elif(player == computer):
        worl = "Remis"
    else:
        worl = "Przegrałeś"

    print(f"Komputer wybrał {cchoice}, {worl}!", end="\n\n")




main()