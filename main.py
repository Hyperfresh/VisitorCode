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
import time # Time module for sleep and retrieval of current time.
import getpass # PIN module.
import os # Get OS details and run clearscreen.
import platform # Get OS details.
import ctypes # Get admin details.
from pathlib import Path # Check for existing file. THIS MAY NOT BE INSTALLED
import csv # CSV is a bit of a mess, but...

# One of the liibraries above MAY NOT BE INSTALLED on your computer.
# To fix this, run pip. On mac0S, assuming you have Python 3.7, run "pip3.7 install keyboard" etc. Sudo may be required.
# On Windows, run "python -m pip install keyboard" etc.

# Functions
def UpdateTime(): # A handy shortcut to update the Time variable
    global CurrentTime
    CurrentTime = (time.strftime("%d %b %Y %H:%M:%S", time.localtime()))


def clear(): # Clear screen module. The command for clearing the screen in Posix is different to Windows.
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')

def isAdmin(): # su check module
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def checkfile(): # if database already exists
    global option
    my_file = Path("database.txt")
    if my_file.is_file():
        file1 = open('database.txt','r')
        alist = file1.read().splitlines()
        if alist != ['Name,Phone,PIN,Sign-in status,Timestamp']:
            print("It looks like there's exisitng data in the database:")
            print('\n'.join(alist))
            file1.close #close file
            print("\nWhat do you want to do? You can either clear the database or write to the existing database.")
            def chooseoption():
                global option
                print(colored("For verification purposes, please enter 'clear' or 'write'.","yellow"))
                option = input(colored("WARNING: ","red") + "Clearing the database cannot be undone. > ")
                if option == "clear":
                    file2 = open('database.txt','w')
                    file2.write("Name,Phone,PIN,Sign-in status,Timestamp\n")
                    file2.close
                    print(colored("File cleared.\n","green"))
                elif option != "write":
                    print(colored("Sorry, please try that again.","red"))
                    chooseoption()
                else:
                    print(colored("Writing to existing file.\n","green"))
            chooseoption() #call to choose option
        else:
            file2 = open('database.txt','a')
            file2.close
    else:
        file2 = open('database.txt','w')
        file2.write("Name,Phone,PIN,Sign-in status,Timestamp\n")
        file2.close

def pinchecker():
    global pin
    try:
        pin = int(getpass.getpass("Please enter a PIN. > "))
        if len(str(pin)) != 4:
            print(colored("Your PIN must be exactly 4 numbers long.","red"))
            pinchecker()
        pincheck = int(getpass.getpass("Enter the PIN again > "))
        if pincheck != pin:
            print(colored("Sorry, the PINs you entered didn't match.","red"))
            pinchecker()
    except:
        print(colored("Sorry, please try that again.","red"))
        pinchecker()

# String checks if it can be converted to a number.
def NumCheck(Prompt):
    global NumberToCheck
    NumberToCheck = str((input(Prompt + " > ")))
    try:
        NumberToCheck = int(NumberToCheck)
    except:
        print(colored("Sorry, please try that again.","red"))
        NumCheck(Prompt)

    if len(str(NumberToCheck)) != 9:
        print(colored("A phone number should have nine digits, excluding the 0 at the beginning.","red"))
        NumCheck(Prompt)

# PIN
def pinput(admin):
    global userinput
    global AdminPIN
    if admin == True:
        try:
            userinput = int(getpass.getpass("> "))
        except:
            print(colored("Sorry, please try that again.","red"))
            pinput(True)

        if len(str(userinput)) != 4:
            print(colored("Sorry, please try that again.","red"))
            pinput(True)
        
        if userinput != AdminPIN:
            print(colored("Sorry, that PIN you entered is wrong.","red"))
            correct = False
        else:
            correct = True
        
        return correct
    else:
        try:
            userinput = int(getpass.getpass("> "))
        except Exception as e:
            print(e)
            print(colored("Sorry, please try that again.","red"))
            pinput(False)

        if len(str(userinput)) != 4:
            print(colored("Sorry, please try that again.","red"))
            pinput(True)

def write_cell(row, col, val): # Overwriting data. Thanks @GradyDal on Repl.it
	with open('database.csv') as f:
		data = list(csv.reader(f))
		data[int(row)][int(col)] = val
		new_data = open('database.csv', 'w', newline = '')
		csv_writer = csv.writer(new_data)
		csv_writer.writerows(data)
		new_data.close()

def read_cell(row, col): # Getting name of entry. Again, thanks @GradyDal
	with open('database.csv', 'r') as f:
		data=list(csv.reader(f))
		return(data[int(row)][int(col)])

#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################

# Start-up screen
print("")
UpdateTime()
print("Concordia College Visitor Application")
print(CurrentTime)
print(os.name + " " + platform.system() + " " + platform.release())
print("")

if os.name == "posix": # Because the keyboard library requires su on Unix, this code checks   
    if isAdmin(): # Prints warning.
        print(colored("You are running this application on a Unix device. Some things may not work properly.","yellow"))
        print("")
    else: # Prints error and exits.
        print(colored("You are running this application on a Unix device without su privileges. Please run this application with su.","red"))
        exit()

checkfile() # call to check if database exists

print("You are about to set an Administration PIN.\nRemember it as you will need it to view the database\nand close the application.")
pinchecker()
AdminPIN = pin

print("\nDo you want to convert the database to a CSV file at close of application? (y/n)")
print(colored("NOTE: ","yellow") + "Converting the database at close will no longer make it accessible to this application.\nThis may be useful if you plan to start with new databases every program start-up,\nwhile still keeping an archival record of previous entries.")
convertfile = False
while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('n'):
                print(colored("Not converting file.","cyan"))
                break
            if keyboard.is_pressed('y'):
                convertfile = True
                print(colored("Converting file.","cyan"))
                break
        except:
            break  # if user pressed a key other than the given key the loop will break

print("\nOkay, now that's set. You won't see it on the UI as it's meant to be unattended -\npress [Escape] to close the application, and [?] to view the database.\n")
print("Loading...")
time.sleep(5)
print("")

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
                    (or visited before)                                                                  ___/"""

# Visitor module
def Visitor():
    global NumberToCheck
    global name
    global phone
    global pin
    global pincheck
    global sign
    global CurrentTime
    global reset
    name = str(input("Please enter your name. > "))
    NumCheck("Enter your phone number.")
    phone = NumberToCheck
    if reset == True:
        searchfile = open("database.txt", "r")
        linenum = 1
        found = False
        for line in searchfile:
            linenum = linenum + 1
            if (str(name) + "," + str(phone)) in line:
                found = True
                print("Your entry " + str(name) + " with phone number 0" + str(phone) + " will be reset. Confirm? (y/n)")
                searchfile.close

        if found == False:
            print(colored("Your entry could not be found or verified.","red"))
            searchfile.close
            time.sleep(5)
            UI()

    else:
        searchfile = open("database.txt", "r")
        linenum = 1
        found = False
        for line in searchfile:
            linenum = linenum + 1
            if ("," + str(phone)) in line:
                found = True
                searchfile.close

        if found == True:
            print(colored("It seems that phone number is registered onto someone else.\nPlease contact Admin if you think this is a mistake.","red"))
            searchfile.close
            time.sleep(5)
            UI()

        print("An entry for " + str(name) + " with phone number 0" + str(phone) + " will be created. Confirm? (y/n)")
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('n'):
                print("Okay, cancelling.")
                time.sleep(5)
                UI()
            if keyboard.is_pressed('y'):
                break
        except:
            break  # if user pressed a key other than the given key the loop will break
    print(colored("You are about to set a PIN. It must be numeric and cannot start with 0.","yellow"))
    pinchecker()
    if reset == False:
        sign = True
        UpdateTime()
        file2 = open('database.txt', 'a')
        file2.write(str(name) + ',')
        file2.write(str(phone) + ',' + str(pin) + ',' + str(sign) + ',' + str(CurrentTime) + " \n")
        file2.close()
        print("Thank you, " + str(name) + ".")
        print("You have been signed in. Please remember your PIN.")

    else:
        sign = False
        os.rename("database.txt","database.csv")
        write_cell(linenum-1, 2, pin)
        UpdateTime()
        write_cell(linenum-1, 4, CurrentTime)
        os.rename("database.csv","database.txt")
        print("Thank you, " + str(name) + ".")
        print("Your account has been successfully reset.\nPlease sign in by pressing [2] on the next screen.")
    
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
    global userinput
    NumCheck("Enter your phone number.")
    searchfile = open("database.txt", "r")
    linenum = 1
    for line in searchfile:
        linenum = linenum + 1
        if str(NumberToCheck) in line:
            if "False" in line:
                print("Entry found, please enter your PIN.")
                pinput(False)
                if ("," + str(userinput) + ",") in line:
                    sign = True
                    os.rename("database.txt","database.csv")
                    write_cell(linenum-1, 3, sign)
                    UpdateTime()
                    write_cell(linenum-1, 4, CurrentTime)
                    print("Thank you, " + read_cell(linenum-1, 0) + ".\nYou have been signed in.")
                    os.rename("database.csv","database.txt")
                else:
                    print(colored("The PIN you entered does not match the PIN in the database.","red") + " Returning to UI.")
            else:
                print(colored("It looks like you've already signed in.","red") + " Returning to UI.")
            searchfile.close()
            time.sleep(5)
            UI()
    print(colored("The phone number you entered cannot be found in the database.","red") + " Returning to UI.")    
    searchfile.close()
    time.sleep(5)
    UI()
    

# Sign out module
def SignOut():
    global NumberToCheck
    global name
    global phone
    global pin
    global pincheck
    global sign
    global CurrentTime
    global userinput
    NumCheck("Enter your phone number.")
    searchfile = open("database.txt", "r")
    linenum = 0
    for line in searchfile:
        linenum = linenum + 1
        if str(NumberToCheck) in line:
            if "True" in line:
                print("Entry found, please enter your PIN.")
                pinput(False)
                if ("," + str(userinput) + ",") in line:
                    sign = False
                    os.rename("database.txt","database.csv")
                    write_cell(linenum-1, 3, sign)
                    UpdateTime()
                    write_cell(linenum-1, 4, CurrentTime)
                    thename = read_cell(linenum-1, 0)
                    print("Thank you, " + thename + ".\nYou have been signed out.")
                    os.rename("database.csv","database.txt")
                else:
                    print(colored("The PIN you entered does not match the PIN in the database.","red") + " Returning to UI.")
            else:
                print(colored("It looks like you've already signed out.","red") + " Returning to UI.")
            searchfile.close()
            time.sleep(5)
            UI()
    print(colored("The phone number you entered cannot be found in the database.","red") + " Returning to UI.")    
    searchfile.close()
    time.sleep(5)
    UI()
    
# User interface module
def UI():
    global reset
    global CurrentTime
    clear()
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
            if keyboard.is_pressed('3'):
                SignOut()
            if keyboard.is_pressed('4'):
                reset = True
                Visitor()

            if keyboard.is_pressed('esc'):
                print(colored("Escape pressed. Please enter Administration PIN.","yellow"))
                if pinput(True):
                    print("Exiting...")
                    if convertfile == True:
                        CurrentTime = (time.strftime("%d_%b_%Y_%H-%M-%S", time.localtime()))
                        os.rename("database.txt","database_" + str(CurrentTime) + ".csv")
                    time.sleep(1)
                    exit()
                else:
                    time.sleep(5)
                    UI()
            if keyboard.is_pressed('?'):
                print(colored("Query requested. Please enter Administration PIN.","yellow"))
                if pinput(True):
                    file1 = open('database.txt','r')
                    alist = file1.read().splitlines()
                    if alist != ['Name,Phone,PIN,Sign-in status,Timestamp']:
                        print('\n'.join(alist))
                    else:
                        print(colored("It looks like the database is empty.","cyan"))
                    try:
                        input("Press the [Enter] key to return to UI.")
                    except:
                        UI()
                    UI()
                else:
                    time.sleep(3)
                    UI()

        except Exception as e:
            print(e)
            break

# And this is the thing that calls it. Pretty boring I know.
UI()