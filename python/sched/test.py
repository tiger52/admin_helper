#!/usr/bin/env python
import sched, time
import os,signal

pidfile = "test.pid"
# look pid, if exist stop proccess
if os.path.isfile(pidfile):
	print "pid exist"
	with open(pidfile,'r') as f:
		pid = f.read
		print "PID={}".format(pid)
		#os.kill(pid, signal.SIGKILL)
		#print "proccess killed"
		#os.system('rm {}'.format(pid))
		#print "latest pid file deleted"
		exit

# Write the PID file
with open(pidfile,'w') as f:
	print >> f, os.getpid()
s = sched.scheduler(time.time, time.sleep)
def print_time(): print "From print_time", time.ctime()

while True:
	def print_some_times():
	    print time.ctime()
	    s.enter(5, 1, print_time, ())
	    s.enter(10, 1, print_time, ())
	    s.run()
	    print time.ctime()

	print_some_times()
