#!/usr/bin/env python
import socket	# for using UDP
import struct	# for using UDP
import sys, os
import time, datetime
import getopt	# for menu
import logging


blackoutlog = logging.getLogger('blackout')
server_my = 2000
#timerStart1 = time.mktime(time.strptime("2015-12-28 11:41:00", "%Y-%m-%d %H:%M:%S"))
#timerEnd1 = time.mktime(time.strptime("2015-12-28 11:42:00", "%Y-%m-%d %H:%M:%S"))
#timelist = [[timerStart1,timerEnd1],[timerStart2,timerEnd2]]


def startMulticasting(multicast_channel1, server_port, record_list, filename):
	""" change input channel depending on blackout list
	multicast_channel1 - main channel (ip string)
	server_port - it's a port on wich we receive and sent packets
	record_list like [[timeStart1,timeEnd2], [timeStart1,timeEnd2], ...]
	"""
	
	sockin1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	sockin1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sockin1.bind((multicast_channel1, server_port))
	
	ch1aton = socket.inet_aton(multicast_channel1)
	mreq1 = struct.pack('4sL', ch1aton, socket.INADDR_ANY)
	sockin1.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq1)

	#before start
	picturefilename = "{0}.ts".format(filename)
	picturefile = open(picturefilename, 'w')
	# Receive/respond loop
	print "starting record"
	blackoutlog.info("starting record")
	while True:
		now = time.time()
	#	data, address = sockin1.recvfrom(1316)
		if now >= record_list[0] and now <= record_list[1]:
			#data, address = sockin1.recvfrom(1316)
			data = sockin1.recv(1316)
			picturefile.write(data)
		if now > record_list[1]:
			break
	picturefile.close()
	print "saved file {0}".format(picturefilename)
	print "Done."
	blackoutlog.info("saved file {0}\nDone.".format(picturefilename))
	
		
# main Function
#def startSched(nameOfFile, multicast_to_sent):
#	blackoutlog.info("Open the file '{0}', and start scheduling...".format(nameOfFile))
#	name, expanse = nameOfFile.rsplit(".",1)
#	pidfile = nameOfFile + ".pid"
#	with open(pidfile, 'w') as f:
#		f.write(str(os.getpid()))
#	if  expanse == "xls":
#		toStream = getXLS(nameOfFile)
#		startMulticasting(toStream[0], multicast_zaglushka, server_my, multicast_to_sent, toStream[1])
#	elif expanse == "xml":		
#		toStream = getXML(nameOfFile)
#		startMulticasting(toStream[0], multicast_zaglushka, server_my, multicast_to_sent, toStream[1])
#	os.remove(pidfile)

# === Main program
def usage():
	print "-h,--help\tprint this help"
	print "-i,--input\tudp address input, format - 239.32.4.110"
	print "-f,--file\tname of file"
	print "-b,--begin\tset start time, format - 2015-01-01 11:00:00"
	print "-s,--stop\tset stop time, format - 2015-01-01 11:30:00" 
	print "EXAMPLE: python record.py --input \"239.32.4.110\" --file trololo.ts --begin \"2015-01-01 11:00:00\" --stop \"2015-01-01 11:30:00\""

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hi:f:b:s", ["help", "input=", "file=", "begin=", "stop="])
	except getopt.GetoptError, err:
		print str(err) # will print something like "option -a not recognized"
		usage()
		sys.exit(2)
	file = None
	if not opts:
		usage()
		sys.exit()
	for option, value in opts:
		if option in ("-h", "--help", ""):
			usage()
			sys.exit()
		elif option in ("-i", "--input"):
			inputstream = value
		elif option in ("-f", "--file"):
			outputfile = value
		elif option in ("-b", "--begin"):
			begintime = value
		elif option in ("-s", "--stop"):
			stoptime = value
		elif option is None:
			usage()
			sys.exit()
		else:
			assert False, "unhandled option"
#	startSched(filesched, outstream)
	# logging setings
	outputfile = outputfile + "{0}".format(time.time())
	fh = logging.FileHandler('{0}.log'.format(outputfile))
	frmt = logging.Formatter('%(asctime)s - %(levelname)-8s - %(message)s')
	fh.setFormatter(frmt)
	blackoutlog.addHandler(fh)
	blackoutlog.setLevel(logging.INFO)
	blackoutlog.debug('test debug level')
	#blackoutlogger.info('test blackout log info level')
	blackoutlog.info("value from input - {0} - {1} - {2} -{3}".format(inputstream, outputfile, begintime, stoptime))

	timerStart1 = time.mktime(time.strptime(begintime, "%Y-%m-%d %H:%M:%S"))
	timerEnd1 = time.mktime(time.strptime(stoptime, "%Y-%m-%d %H:%M:%S"))
	timelist = [timerStart1,timerEnd1]
	startMulticasting(inputstream, server_my, timelist, outputfile)
if __name__ == "__main__":
	main()
