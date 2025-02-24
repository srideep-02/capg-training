import threading
import time

def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has acquired the lock")
        time.sleep(2)
        print(f"{threading.current_thread().name} has released the lock")
        
lock=threading.Lock()
thread=[threading.Thread(target=task,args=(lock,)) for _ in range(3)]
for t in thread:
    t.start()
for t in thread:
    t.join()
    
print("Exited")