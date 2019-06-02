import time
from Queue import Queue
from threading import Thread

query1 = [ "123", "234", "345" ]
query2 = [ "234", "345", "456" ]
def worker():
    while True:
        item = q.get()
        print "start worker {} at {}".format(item,time.time())
        time.sleep(10)
        print "end worker {} at {}".format(item,time.time())
        q.task_done()

q = Queue()
num_worker_threads = 3
for i in range(num_worker_threads):
     t = Thread(target=worker)
     t.daemon = True
     t.start()

#items = [ "qwe", "asd", "zxc" ]
#for item in items:
#    q.put(item)
#    time.sleep(1)
#q.join() 
count = 1
while True:
    print "queue - {}".format(count)
    q.put(count)
    count = count + 1
    time.sleep(3)
