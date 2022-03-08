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
```console
$ python3 hue.py
```



## About this tool
This is a project that I created after noticing HTTP traffic coming from my personal Hue Bridge. 
I do not condone or encourage using this tool on any lights that you do not own or have permission to access / control. 
In its current state, it requires authenticating with the bridge by pressing the button on the bridge.
In the future I would like to add the ability to send get requests to the bridge and then output the data in the various JSON files in a easier to read format that can be used to quickly identify devices that have connected to the bridge, the apps that have been used with the bridge and other various pieces of information I noticed in the HTTP traffic with no prior authentication. 

I hope that as I work on this project I will gain more real world experience working with python.
