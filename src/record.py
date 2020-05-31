'''
This program records your mouse and keyboard inputs and replays them.
'''
import os
import threading
import mouse
import keyboard
import pyautogui
import pickle
import time


width = pyautogui.size()[0]
height = pyautogui.size()[1]
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mouse_events = []

#a
mouse.hook(mouse_events.append)
keyboard.start_recording()
time.sleep(.2)
#we move to arbitrary position and press a harmless key so the keyboard and mouse events start recording at the same time.

pyautogui.moveTo(width/2,height/2) #move mouse to middle of screen
pyautogui.press('left')

keyboard.wait("`") #press this key to stop recording

mouse.unhook(mouse_events.append)
keyboard_events = keyboard.stop_recording()
print(base_dir)
pickle.dump(mouse_events,open(base_dir + r'/events/mouse.p','wb'))
pickle.dump(keyboard_events,open(base_dir + r'/events/keyboard.p','wb'))
