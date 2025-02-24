import threading
import time

def task1():
    for i in range(5):
        print(f"Task 1 - Count {i}")
        time.sleep(0)

def task2():
    for i in range(5):
        print(f"Task 2 - Count {i}")
        time.sleep(0)

# Creating threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Starting threads
thread1.start()
thread2.start()

# Waiting for both threads to finish
thread1.join()
thread2.join()

print("Both tasks completed!")