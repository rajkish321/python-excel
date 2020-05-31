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

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mouse_events = []

#
mouse.hook(mouse_events.append)
keyboard.start_recording()
time.sleep(.2)
#we move to arbitrary position and press a harmless key so the keyboard and mouse events start recording at the same time.
pyautogui.moveTo(500,200)
pyautogui.press('left')

keyboard.wait("a")

mouse.unhook(mouse_events.append)
keyboard_events = keyboard.stop_recording()
#Keyboard threadings:
k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events))
k_thread.start()

#Mouse threadings:

m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))
m_thread.start()

#waiting for both threadings to be completed

k_thread.join()
m_thread.join()
