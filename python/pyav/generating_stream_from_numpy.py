from __future__ import division
import av
import numpy as np
from ctypes import cdll
import time
av_format = cdll.LoadLibrary("libavformat")

duration = 60
fps = 25
total_frames = duration * fps

#out = av.open('test.mp4', mode='w')
print "open rtmp stream"
out = av.open('rtmp://172.30.120.246:1935/myapp/pythontest', file='0')
print "rtmp opened"

#stream = out.add_stream('mpeg4', rate=fps)
stream = out.add_stream('libx264', rate=fps)
stream.width = 1280
stream.height = 720
stream.pix_fmt = 'yuv420p'

print "generating..."
for frame_i in range(total_frames):

    img = np.empty((1280, 720, 3))
    img[:, :, 0] = 0.5 + 0.5 * np.sin(2 * np.pi * (0 / 3 + time.time() / total_frames))
    img[:, :, 1] = 0.5 + 0.5 * np.sin(2 * np.pi * (1 / 3 + time.time() / total_frames))
    img[:, :, 2] = 0.5 + 0.5 * np.sin(2 * np.pi * (2 / 3 + time.time() / total_frames))

    img = np.round(255 * img).astype(np.uint8)
    img = np.clip(img, 0, 255)

    frame = av.VideoFrame.from_ndarray(img, format='rgb24')
    packet = stream.encode(frame)

    if packet:
        out.mux(packet)
        print "packet muxed"
#    for packet in stream.encode(frame):
#        container.mux(packet)

# Flush stream
#for packet in stream.encode():
#    out.mux(packet)
print "Flush stream"
while True:
    out_packet = stream.encode()
    if out_packet:
        out.mux(out_packet)
    else:
        break

# Close the file
out.close()
