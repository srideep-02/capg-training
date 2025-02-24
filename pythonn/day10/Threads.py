import threading
import time
 
def task():
    print("Thread started")
    time.sleep(2)
    print("Thread stopped")
    

def numbers():
    for i in range(10):
        time.sleep(2)
        if (i%2==0):
            print(f"The even numbers are{i}") 
        else:
            print(f"The odd numbers are{i}")
    
            
thread=threading.Thread(target=task)
thread1=threading.Thread(target=numbers)

thread.start()
thread.join()
print("first thread execution completed")

thread1.start()

thread1.join()
print("second thread execution completed")