#!/usr/bin/python
import requests
import os
from config import *
from phue import Bridge
lights = Bridge.lights

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def printHeader():
    print(30 * "-" , "HUE APP" , 30 * "-")

#def bridgeConnect():
#    target = input("Please enter the IP Address of your Hue Bridge: ")
#    b = Bridge(target)
#    b.connect()



def printOnOffMenu():
    printHeader()
    print("1. Turn the lights on")
    print("2. Turn the lights off")
    print("")
    print("[3.] Exit back to main menu")

    onoffselect = int(input("Please select your option: "))
    while onoffselect != 0:
        if onoffselect == 1:
            onoffselect = 0
            print("Turning Lights On")
            hueOn()
            printOnOffMenu()
        if onoffselect == 2:
            onoffselect = 0
            print("Turning Lights off")
            hueOff()
            printOnOffMenu()

        if onoffselect == 3:
            onoffselect = 0
            printMainMenu()
        else:
            input("Please make sure you specified the correct option!")

            onoffselect = 0


def hueOn():
        b = Bridge(target)
        b.set_light(selectedLights,'on', True)
def hueOff():
        b = Bridge(target)
        b.set_light(selectedLights,'on', False)


def discoverLights():
        b = Bridge(target)
        lights = b.get_light_objects('id')
        print(lights)

def auth():
    b = Bridge(target)
    b.connect()



def colorMenu():
    printHeader()
    print("[1.] Green")
    print("[2.] Blue")
    print("[3.] Purple")
    print("[4.] Pink")
    print("[5.] Red")
    print("[6.] Orange")
    print("[7.] Yellow")
    colorChoice = int(input("Please Select the color: "))

    while colorChoice != 0:
        if colorChoice == 1:
            colorChoice = 0
            print("green")
        elif colorChoice == 2:
            colorChoice = 0
            print("Blue")
        elif colorCoice == 3:
            colorChoice = 0
            print("Purple")
        elif colorChoice == 4:
            colorChoice = 0
            print("Pink")
        elif colorChoice == 5:
            colorChoice = 0
            print("Red")
        elif colorChoice == 6:
            colorChoice = 0
            print("Orange")
        elif colorChoice == 7:
            colorChoice = 0
            print("Yellow")


# send get requests hue bridge to get status of bulbs
# uncomment when building recon tool
#r = requests.get(target)



def printMainMenu():
    printHeader()
    print("[1.] Authenticate with bridge (Only needs to be done once)")
    print("[2.] Discover Hue lights")
    print("[3.] Turn Lights On/Off")
    print("[4.] Color Menu")
    print("")
    print("[5.] Exit")
    selection = ''
    while selection != 0:
        selection = int(input("Please select your option: "))
        if selection == 1:
            selection = 0
            auth()
            printMainMenu()
        elif selection == 2:
            selection = 0
            discoverLights()
            printMainMenu()
        elif selection == 3:
            selection = 0
            printOnOffMenu()
        elif selection == 4:
            selection = 0
            colorMenu()
        elif selection == 5:
            selection = 0
            return
        else:
            input("Please make sure you specified the correct option!")
            #try putting while loop into function so that the error message is displayed and then re-opens in the menu
            selection = 0

#selection = int(input("Please select your option: "))
printMainMenu()
