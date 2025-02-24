import threading
import time

data=[
    list(range(1,10)),
    list(range(10,20)),
    list(range(20,30)),
    list(range(30,40))
]

def process(data,i):
    start=time.time()
    print(f"Sum of {data[0]},to {data[-1]}is {sum(data)}")
    end = time.time()
    print(f"Thread {i} took {end-start},ns")
    
threads = []
i=0
for d in data:
    i+=1
    t1 = threading.Thread(target=process,args=(d,i))
    threads.append(t1)
    t1.start()
    
for t1 in threads:
    t1.join()
    
print("All threads are completed")    