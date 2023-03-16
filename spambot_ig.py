'''
    Description: Send messages from python to instagram.
    Author: aulerjbailey
    Video: https://youtu.be/P23eUMc6vEE
'''
import pyautogui
from time import sleep

sleep(5)

# open a simple file
with open('test.txt','r') as file:
    # iterate
    for line in file:
        # write the lines on page opened
        pyautogui.typewrite(line)

        # press enter (send message)
        pyautogui.press("enter")