import socket
import struct
import sys

# channels
ch1 = '239.32.4.110'
ch2 = '239.32.5.251'
chport = 2000
interface = '172.30.31.166'
IFACE = "bond0.601"
# socket sent
multicast_sent = ('239.32.7.110', 2000)

# socket receive
sockin1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sockin1.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, IFACE)
sockin1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sockin1.bind((ch1, chport))
ch1aton = socket.inet_aton(ch1)
mreq1 = struct.pack('4sL', ch1aton, socket.INADDR_ANY)
sockin1.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq1)
#sockin1.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(interface))

sockin2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sockin2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sockin2.bind((ch2, chport))
ch2aton = socket.inet_aton(ch2)
mreq2 = struct.pack('4sL', ch2aton, socket.INADDR_ANY)
sockin2.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq2)

# Create the datagram socket
sock_sent = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set the time-to-live for messages to 1 so they do not go past the local network segment.
mreqsent = struct.pack('4sL', socket.inet_aton('239.32.7.110'), socket.INADDR_ANY)
sock_sent.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreqsent)
ttl = struct.pack('B', 127)
sock_sent.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


while True:
        data1, address1 = sockin1.recvfrom(1316)
	sent = sock_sent.sendto(data1, multicast_sent)

