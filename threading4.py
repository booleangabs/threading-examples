import threading
import random
import sys

NUMBER = random.randint(1, 10)


def timerTarget():
    global NUMBER
    print("Time is up")
    NUMBER = random.randint(1, 10)


t0 = threading.Timer(10, timerTarget)
t0.start()

while True:
    answer = input("> ")
    if int(answer) == NUMBER:
        print("You win")
        t0.cancel()
        break
