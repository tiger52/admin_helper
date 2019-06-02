#!/usr/bin/env python
from threading import Thread
import subprocess
from Queue import Queue
import re

num_ping_threads = 3
in_queue = Queue()
ips = ["172.30.5.182", "172.30.5.105", "172.30.5.121", "172.30.5.111"]

def pinger(i, iq):
	"""asking network"""
	while True:
		ip = iq.get()
		print "Thread %s: Pinging %s" % (i, ip)
		ret = subprocess.call("ping -c 1 %s" % ip, shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
		print "ret : {}".format(ret)
		if ret == 0:
			print "%s: is alive" % ip
		else:
			print "%s: did not respond" % ip
		iq.task_done()

for ip in ips:
	in_queue.put(ip)

for i in range(num_ping_threads):
	worker = Thread(target=pinger, args=(i, in_queue))
	worker.setDaemon(True)
	worker.start()

print "Main Thread Waiting"
in_queue.join()
print "Done"
