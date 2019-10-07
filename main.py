from scrtinf import s1
from scrtinf import s2
from scrtinf import s3
from scrtinf import s4
from scrtinf import s5
scertyiatmpt = ""
usnac = "PickyProgram"
pwacid = "VerySecretpass"
pwscatmpt = ""
acidscrt = "n0Bodyguessd"
idscrtatmpt = ""

idscrtatmpt = input("Enter username. ")
if idscrtatmpt == usnac:
    print("Correct username.")
    scertyiatmpt = input("Enter password. ")
    if scertyiatmpt == pwacid:
        print("Correct password.")
        pwscatmpt = input("Enter the loginID. ")
        if pwscatmpt == acidscrt:
            print("Welcome, Vemund Niillas. Here is all your Information.")
            print(s1)
            print(s2)
            print(s3)
            print(s4)
            print(" ")
            print(s5)
