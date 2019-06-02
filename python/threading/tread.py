#!/usr/bin/env python
import threading
import time

count = 1
class KissThread(threading.Thread):
	def run(self):
		global count
                idp = count
		print("{0} - thread number {1}: Pretending to do stuff".format(time.ctime(), idp))
		count += 1
		time.sleep(2 + count)
		print("{0} - done {1}".format(time.ctime(), idp))

for t in range(5):
	KissThread().start()


