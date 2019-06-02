# === server Multicast
# Receive and retranslate multicast message

import socket
import struct
import sys

sockIN = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockIN.bind(('', 2000))

ch1 = socket.inet_aton('239.32.7.55')
ch2 = socket.inet_aton('239.32.7.56')


mr1 = struct.pack('4sL', ch1, socket.INADDR_ANY)
mr2 = struct.pack('4sL', ch2, socket.INADDR_ANY)

sockIN.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mr1)
sockIN.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mr2)

while True:
        print >>sys.stderr, '\nwaiting to receive message'
        data1, address1 = sockIN.recvfrom(1024)
        data2, address2 = sockIN.recvfrom(1024)
        print >>sys.stderr, 'received %s bytes from %s' % (len(data1), address1)
        print >>sys.stderr, 'data is - %s' % data1
        print >>sys.stderr, 'received %s bytes from %s' % (len(data2), address2)
        print >>sys.stderr, 'data is - %s' % data2


