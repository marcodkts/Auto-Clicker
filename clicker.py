class AutoClicker:
    import time
    from threading import Thread
    from pynput.mouse import Controller, Button
    from pynput.keyboard import Listener, KeyCode

    def __init__(self):
        self.clicking = False
        self.toggleKey = None
        self.mouse = self.Controller()
        self.running = True

    def clicker(self):
        while self.running:
            if self.clicking:
                self.mouse.click(self.Button.left, 1)
            self.time.sleep(0.0001)

    def toggleEvent(self, key):
        if key == self.toggleKey:
            self.clicking = not self.clicking

    def startListener(self):
        with self.Listener(on_press=self.toggleEvent) as self.listener:
            self.listener.join()

    def startThreads(self):
        click_thread = self.Thread(
            name="clickerThread",
            target=self.clicker,
            daemon=True
        )
        listener_thread = self.Thread(
            name="listenerThread",
            target=self.startListener,
            daemon=True
        )
        click_thread.start()
        listener_thread.start()

    def startClicker(self, toggleKey):
        self.running = True
        self.toggleKey = self.KeyCode(char=toggleKey)
        self.startThreads()

    def stopClicker(self):
        self.clicking = False
        self.running = False
        self.listener.stop()
