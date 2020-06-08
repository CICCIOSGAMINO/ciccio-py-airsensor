py-airsensor
============
[TOC]

Simple python script to handle a adafruit airsensor 

https://github.com/CICCIOSGAMINO/py-airsensor

## env 
To use the app you need two environment variable with valid values: 

+ PY_CLIENT=adafruit_client
+ PY_KEY=adafruit_api_key

## ssh 
Activate the ssh service:
```bash
# get the user 
who 
# activate the ssh 
sudo systemctl enable ssh
sudo systemctl start ssh 
```

Now you can connect to the device: 
```bash
ssh pi@192.168.1.57 
```

## Snap 
Instsall snap 
```bash
sudo apt update 
sudo apt install snapd 
sudo reboot 
```
