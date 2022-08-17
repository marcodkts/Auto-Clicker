class AutoClicker:
    import time
    import threading
    from pynput.mouse import Controller, Button
    from pynput.keyboard import Listener, KeyCode

    def __init__(self):
        self.clicking = False
        self.toggleKey = None
        self.mouse = self.Controller()

    def clicker(self):
        while True:
            if self.clicking:
                self.mouse.click(self.Button.left, 1)
            self.time.sleep(0.0001)

    def toggleEvent(self, key):
        if key == self.toggleKey:
            self.clicking = not self.clicking
            print("Running..." if self.clicking else "Stoped    \r", end="\r")

    def startListener(self):
        with self.Listener(on_press=self.toggleEvent) as self.listener:
            self.listener.join()

    def startThread(self):
        click_thread = self.threading.Thread(target=self.clicker)
        click_thread.start()

    def startClicker(self, toggleKey):
        self.toggleKey = self.KeyCode(char=toggleKey)
        self.startThread()
        self.startListener()
