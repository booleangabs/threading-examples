import threading
import time

counter: int = 0


class MyThread(threading.Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.greetingCount = 0

    def run(self):
        while True:
            print(f"Hi, I'm {self.name}. This is my number {self.greetingCount} greeting.")
            self.greetingCount += 1
            time.sleep(1)


t0 = MyThread("Lilly")


def myTarget(name: str):
    global counter
    while True:
        print(f"Hi, I'm {name}. This is my number {counter} greeting.")
        counter += 1
        time.sleep(1)


t1 = threading.Thread(target=myTarget, args=("Maria",))

t0.start()
t1.start()
