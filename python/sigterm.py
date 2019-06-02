# example on SIGTERM
import time, sys, os
import  signal

def SIGKILL():
	sys.stderr.write("\nBye-bye!\n")
	sys.exit(0)
	os.remove('onefile.txt')

def SIGINT():
	sys.stderr.write("\nBye-bye!\n")
	sys.exit(0)
	os.remove('onefile.txt')

try:
	f = open('onefile.txt', 'w')
	while True:
		#f.write("{0} script working...\n".format(time.ctime()))
		print >> f, "{0} script working...".format(time.ctime()) 
		time.sleep(5)
except KeyboardInterrupt:
#except signal.SIGINT:
	SIGINT()	
