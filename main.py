# -*- coding: utf-8 -*-

# This runs on Git!
# Created using Visual Studio Code.
# Repl.it is running Python through BASH. See the .replit file.

# Paul Asencion (Hy~) 11JHAR
# Planning and programming a visitor register
# Concordia College | SACE 740975X

# Library importing
import keyboard # Library checks for keystrokes. THIS MAY NOT BE INSTALLED
from termcolor import colored # Colored terminal output. THIS MAY NOT BE INSTALLED
import time # Time module for sleep and retrival of current time.
import getpass # PIN module.
import os # Get OS details and run clearscreen.
import platform # Get OS details.
import ctypes # Get admin details.
from pathlib import Path # Check for existing file.

# Start up.
def UpdateTime():
    global CurrentTime
    CurrentTime = (time.strftime("%d %b %Y %H:%M:%S", time.localtime()))

print("")
UpdateTime()
print("Concordia College Visitor Application")
print(CurrentTime)
print(os.name + " " + platform.system() + " " + platform.release())
print("")

def clear():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')

if os.name == "posix": # Because the keyboard library requires su on Unix, this code checks    
    def isAdmin(): # su check module
        try:
            is_admin = (os.getuid() == 0)
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin

    if isAdmin():
        print(colored("You are running this application on a Unix device. Some things may not work properly.","yellow"))
        print("")
    else:
        print(colored("You are running this application on a Unix device without su privileges. Please run this application with su.","red"))
        exit()

def checkfile(): # if database already exists
    global option
    my_file = Path("database.txt")
    if my_file.is_file():
        file1 = open('database.txt','r')
        print("It looks like there's an existing database. The data as follows:")
        alist = file1.read().splitlines()
        print(colored("Name, Phone, PIN, Sign-in status, Timestamp","cyan"))
        print(alist)
        print("\nWhat do you want to do? You can either clear the database or write to the existing database.")
        def chooseoption():
            global option
            print(colored("For verification purposes, please enter 'clear' or 'write'.","yellow"))
            option = input(colored("WARNING: ","red") + "Clearing the database cannot be undone. > ")
            if option == "clear":
                os.remove("database.txt")
                print(colored("File cleared.\n","green"))
            elif option != "write":
                print(colored("Sorry, please try that again.","red"))
                chooseoption()
            else:
                print(colored("Writing to existing file.\n","green"))
        chooseoption()
checkfile()

def pinchecker():
    global pin
    global pincheck
    try:
        pin = int(getpass.getpass("Please enter a PIN. > "))
        pincheck = int(getpass.getpass("Enter it again      > "))
        if pincheck != pin:
            print(colored("Sorry, the PINs you entered didn't match.","red"))
            pinchecker()
    except:
        print(colored("Sorry, please try that again.","red"))
        pinchecker()

print("You are about to set an Administration PIN.\nRemember it as you will need it to view the database\nand close the application.")
pinchecker()
AdminPIN = pin

print("Okay, now that's set. You won't see it on the UI as it's meant to be unattended -\npress [Escape] to close the application, and [?] to view the database.")
print("Loading...")
time.sleep(5)
print("")
clear()

# Variable declaration
name = ""
NumberToCheck = 0
phone = 0
pin = 0
pincheck = 0
sign = False
reset = False
CurrentTime = ""

# Big ASCII stuff
logo = """       ! `c `_                                                                                           
    -Tig9g#$$U)x                                                                                         
  !Yd#@@QDEEB@@QXr-                                                                                      
  xIXmoTT*:v}cIsyd-      `)IM5k^  `voMqz*  'hUv  :hh.  roqMj\` `*zMMI)` `hhhhIV*  Yhhhj}<  -hh,   ^33^   
 !O  -(_ YYr !). *O`    ~B@0VwQO=~#@0Vk8@Q-_@@@M'*@@,.Q@8wy88^:#@gVV$@B;`@@EyX#@m g@QkKB@Q-=@@<  _#@@#>  
XM   qv!`Uhi`Ev_  -8_   g@Q      Q@P    #@o_@@0@#M@@,w@#      E@B    Q@Q`@@OTyB@V g@e  `B@h=@@< `B@IL@#, 
_$-`^*irrUUV*r]*" xw    V@@L:!V}_y@#L:!u@@>_@@r=B@@@,;@@u!:lk"L@@u::L@@V`@@0q@@y  g@b!^K@@^=@@< d@@#B@@Q`
 iY`uVVVyUhoVVVV^ Q`     ^d#@@Bm: (9#@@BW! _##* `3##_ =Z#@@BZ= *5B@@#M~ `##x vB#x d###B$s: !##~v#Q"--:$#j
 Tx  .r^^VeY<x_   g'                                                                                     
 $.  )x)x>uxvLL   ux     'x}L}},  rTLYT^  _y     `z      cYiiii- `?TLYl^ `kLiiii'                        
r6   )xrx>uxvYL   .g    vR-   `_'$~    r0`!#     .#      Q'     -$:    . `#                              
3]   )is}rVLkhY    8'   Q*      vK      R~!#     .#      Qliii* }y  .xxy:`#Liii<                         
d)   ';6!qKyTc"    R_   }6`    _-8:    =g`!#     .#      Q'     ,g-    K*`#                              
,s}r=:!!"=:!:!::<xVT     _l}L}u: `xuYLu?  _WLLLL<`HLLLLr o}iiii_ 'YTii}x``aLiiii.                        
  `:;*^^)uy}*^**=-"""
options = """ _________                                                           _________    _______
|         |  \      /  .        .                                   |   ___   |  |         .
|   /|    |   \    /       ___     _|_   ___    __                  |   ___|  |  |______       ___   ___     ___        _|_
|   _|_   |    \  /    |  |___  |   |   |   |  |                    |   ___|  |         |  |  |   | |   |   |   | |   |  |
|_________|     \/     |   ___| |   |   |___|  |                    |_________|  _______|  |  |___| |   |   |___| |___|  |
 _________    ______                                                 _________    _____        ___/                   ___  _____
|   __    |  |                                                      |         |  |                                   |   |   |   |\   |
|    _\   |  |        ___   ___  _|_  __  ___    __ _|_   ___   __  |   /_|   |  |___    ___   __  ___   ___  _|_    |___|   |   | \  |
|   \__   |  |       |   | |   |  |  |   |   |  |    |   |   | |    |     |   |  |      |   | |   |   | |   |  |     |       |   |  \ |
|_________|  |______ |___| |   |  |  |   |___|\ |__  |   |___| |    |_________|  |      |___| |   |___| |___|  |     |     __|__ |   \|
                                                                                                   ___/"""
# String checks if it can be converted to a number.
def NumCheck(Prompt):
    global NumberToCheck
    NumberToCheck = str((input(Prompt + " > ")))
    try:
        NumberToCheck = int(NumberToCheck)
    except:
        print(colored("Sorry, please try that again.","red"))
        NumCheck(Prompt)

# PIN

# Visitor module
def Visitor():
    global NumberToCheck
    global name
    global phone
    global pin
    global pincheck
    global sign
    global CurrentTime
    name = str(input("Please enter your name. > "))
    NumCheck("Enter your phone number.")
    phone = NumberToCheck
    if reset == True:
        # I could put in some code to check if the entry exists...
        print("Your entry " + str(name) + " with phone number 0" + str(phone) + " will be reset. Confirm?")
    else:
        print("An entry for " + str(name) + " with phone number 0" + str(phone) + " will be created. Confirm?")
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('n'):
                print("Okay, cancelling.")
                time.sleep(3)
                UI()
            if keyboard.is_pressed('y'):
                break
        except:
            break  # if user pressed a key other than the given key the loop will break
    print(colored("You are about to set a PIN. It must be numeric and cannot start with 0.","yellow"))
    pinchecker()
    if reset == False:
        sign = True
    # File writing.
    UpdateTime()
    file2 = open('database.txt', 'a')
    file2.write(str(name) + ', ')
    file2.write(str(phone) + ', ' + str(pin) + ', ' + str(sign) + ', ' + str(CurrentTime) + " \n")
    file2.close()
    print("Thank you, " + str(name) + ".")
    if reset == True:
        print("Your account has been successfully reset.\nPlease sign in by pressing [2] on the next screen.")
    else:
        print("You have been signed in. Please remember your PIN.")
    time.sleep(5)
    UI()

# Contractor module
def Contractor():
    global NumberToCheck
    global name
    global phone
    global pin
    global pincheck
    global sign
    global CurrentTime
    NumCheck("Enter your phone number.")
    
    
# User interface module
def UI():
    print(logo)
    UpdateTime()
    print("\nToday is " + CurrentTime + ".")
    print(options)
    while True:
        try:
            if keyboard.is_pressed('1'):
                Visitor()
            if keyboard.is_pressed('2'):
                Contractor()
            if keyboard.is_pressed('esc'):
                print(colored("Escape pressed. Please enter Administration PIN.","yellow"))
                
                exit()
        except:
            break

# And this is the thing that calls it. Pretty boring I know.
UI()