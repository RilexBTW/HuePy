# HuePy
Phillips Hue Tool coded in Python using PHue Library

## Installation
```console
# clone the repo 
$ git clone 

# navigate to the HuePy directory
$ cd HuePy

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## How to use HuePy
First edit config.py and change the target IP Address to your hue bridge IP. This can be found through your router, using the Phillips Hue app or through a tool like netdiscover. In the future this tool will support finding the IP on its own, but until then this will have to be done manually. 

Upon further research, I noticed that Philips actually has a tool for developers that will discover all Hue Bridges connected to your local network, which might be more convenient than any of the other methods mentioned above, but for documentation purposes I'll still mention the other methods.
https://discovery.meethue.com


Once you have finished configuring the config.py file, save the file and now you're ready to run it!

```console
$ python3 hue.py
------------------------------ HUE APP ------------------------------
[1.] Authenticate with bridge (Only needs to be done once)
[2.] Discover Hue lights
[3.] Turn Lights On/Off
[4.] Color Menu
[5.] Help Menu

[10.] Exit

$ Please select your option: ...

```
For first time authentication with a bridge, when prompted to select your option on the main menu, select Authenticate with bridge and now you're ready to have fun!

From here you can list off the Lights that are connected to the bridge. This is a neccessary step with the current build of HuePy in order to control the specific lights you want to control. I know this is inconvenient, so this will be corrected in a future build and was only done for basic functionality at the moment.

At the moment the tool is only able to turn lights On and Off as the Color Menu still needs to be finished. 

The help menu is self explanatory, so I'll leave it at that.

## About this tool
This is a project that I created after noticing HTTP traffic coming from my personal Hue Bridge. 
I do not condone or encourage using this tool on any lights that you do not own or have permission to access / control. 
In its current state, it requires authenticating with the bridge by pressing the button on the bridge.
In the future I would like to add the ability to send get requests to the bridge and then output the data in the various JSON files in a easier to read format that can be used to quickly identify devices that have connected to the bridge, the apps that have been used with the bridge and other various pieces of information I noticed in the HTTP traffic with no prior authentication. 

I hope that as I work on this project I will gain more real world experience working with python.
