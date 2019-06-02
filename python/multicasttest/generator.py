# === server Multicast
# Generate multicast message every time

import socket
import struct
import sys
import time

message = 'very important data 7.56'
multicast_group = ('239.32.7.56', 2000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

while True:
        # Send data to the multicast group
        print >>sys.stdout, 'sending "%s"' % message
        sent = sock.sendto(message, multicast_group)
        time.sleep(2)


