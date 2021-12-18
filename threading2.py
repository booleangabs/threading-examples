import threading
from threading import Thread
from time import sleep


counter = 0


def increment(n):
    global counter

    aux = counter
    aux += n
    sleep(0.5)
    counter = aux
    print(f"Current counter value: {counter}")


t0 = Thread(target=increment, args=(15,))
t1 = Thread(target=increment, args=(10,))

t0.start()
t1.start()

t0.join()
t1.join()

print(counter)
