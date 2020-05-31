import os
import threading
import mouse
import keyboard
import pickle
import pyautogui

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

keyboard.start_recording()
keyboard.stop_recording()

mouse_events = pickle.load(open(base_dir +r'/events/mouse.p','rb'))
keyboard_events = pickle.load(open(base_dir +r'/events/keyboard.p','rb'))

print(keyboard_events)
#Keyboard threadings:
k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events[:-1]))
k_thread.start()

#Mouse threadings:

m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))
m_thread.start()

#waiting for both threadings to be completed

m_thread.join()
k_thread.join()



#
# print(keyboard_events[:-1])
