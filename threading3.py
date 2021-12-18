import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event

    def run(self):
        while True:
            if self.event.is_set():
                print("The main said stop!")
                break
            print(f"Hello, from {self.name}")
            time.sleep(1)


stopEvent = threading.Event()
t0 = MyThread("John", stopEvent)
t0.start()

time.sleep(5)
print("Let's make the thread stop")
stopEvent.set()