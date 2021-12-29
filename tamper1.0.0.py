#TaMper
import platform
import time
import requests
VARIABLEplaceholder = "this is a placeholder"
VARIABLEos = platform.platform()
def checkvar(x):
    if x[0] == "%":
        if x[len(x)-1] == "%":
            return "VARIABLE" + x[1:len(x)-1]
        else:
            return x
    else:
        return x
def checkifvar(br):
    if checkvar(br) != br:
            return checkvar(br)
    else:
        return br
try:
    file = open(input("Please input file name : "),"r")
except FileNotFoundError:
    exit("Error 1 : File does not exist!")

lines = file.readlines()
for line in lines:
    yes = False
    if line.endswith("\n"):
        line = line[:-1]
        yes = True
    if line[0:5] == "speak":
        print(checkifvar(line[6:len(line)]))
        yes = True
    if line[0:4] == "exit":
        exit()
        yes = True
    if line[0:2] == "os":
        print(VARIABLEos)
        yes = True
    if line[0:2] == "lb":
        print("")
        yes = True
    if line[0:4] == "wait":
        time.sleep(int(line[5:len(line)]))
        yes = True
    if line[0:3] == "add":
        exec("VARIABLE" + line[4:len(line)] + " = ''")
        yes = True
    if line[0:3] == "set":
        exec("VARIABLE" + line.split(" ")[1] + " = '" + str(" ".join(line.split(" ")[2:len(line.split(" "))])) + "'")
        yes = True
    elif line[0:3] == "get":
        try:
            a = requests.get(checkifvar(line[4:])).text
            print(a)
        except requests.exceptions.MissingSchema:
            exit("Error 3 : Invalid url protocol, did you mean https://" + line[4:] + "?")
        except requests.exceptions.ConnectionError:
            exit("Error 4 : Unable to connect to url.")
        yes = not yes
    if not yes:
        print("Error 2 : Invalid command. (" + line + ")")
    