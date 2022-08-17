import time
import threading
import os
import psutil
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

PROCNAME = os.path.basename(__file__) if ".py" not in os.path.basename(__file__) else "python.exe"
process_list = [proc.name() for proc in psutil.process_iter()]
if process_list.count(PROCNAME) > 1:
    input("Already running, press enter to exit.")
    exit()

while True:
    TOGGLE_KEY = KeyCode(char=input("Enter a Toggle Key:\n"))
    if input(f"TOGGLE_KEY = {TOGGLE_KEY}, ok? (y/n)\n").lower() == "y":
        break

print(f"Press {TOGGLE_KEY} to start.")
clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.0001)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
        print("Running..." if clicking else "Stoped    \r", end = "\r")


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
