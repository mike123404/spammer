#!/usr/bin/env python3
import pyautogui
import time
from colorama import Fore,Back,Style
import datetime
logo='''
 ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
 |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
     | |                                        
     |_|                by mike                    
'''
print(logo)
x=input(Fore.RED+"type the message you want to spam:     ")
y=int(input(Fore.CYAN+"how many messages do you send:    "))
print(Fore.LIGHTYELLOW_EX+"Sleeping for 10 seconds...")
print(Fore.LIGHTGREEN_EX+"==>Please switch to the desired application.")
time.sleep(10)
time_started=time.time()
a=True
for i in range(y):
    pyautogui.typewrite(x)
    pyautogui.press("enter")
    if a==True:
        print(f"{Back.RED}{Fore.BLACK}{i+1} messages have been sent{Style.RESET_ALL}")
        a=False
    else:
        print(f"{Back.YELLOW}{Fore.BLACK}{i+1} messages have been sent{Style.RESET_ALL}")
        a=True
print(Style.RESET_ALL)
time_lasted=datetime.timedelta(seconds=time.time()-time_started)
print('total time to send the messages:',time_lasted)
