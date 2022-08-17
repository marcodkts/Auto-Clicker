import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
from tools import alreadyRunning

alreadyRunning()

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
