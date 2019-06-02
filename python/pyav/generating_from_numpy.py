from __future__ import division
import av
import numpy as np
import time

width = 1280
height = 720
duration = 60
fps = 25
total_frames = duration * fps

out = av.open('test.mp4', mode='w')

#stream = out.add_stream('mpeg4', rate=fps)
stream = out.add_stream('libx264', rate=fps)
stream.width = 1280
stream.height = 720
stream.pix_fmt = 'yuv420p'
print "generating..."
somevar = 1
for frame_i in range(total_frames):
    img = np.empty((1280, 720, 3))
    img[0:width/3, :, 0] = 0.5 + 0.5 * np.sin(2 * np.pi * (0 / 3 + frame_i / total_frames))
    img[0:width/3, :, 1] = 0.5 + 0.5 * np.sin(2 * np.pi * (1 / 3 + frame_i / total_frames))
    img[0:width/3, :, 2] = 0.5 + 0.5 * np.sin(2 * np.pi * (2 / 3 + frame_i / total_frames))
    img[width/3:width*2/3, :, 0] = 0.5 + 0.5 * np.sin(2 * np.pi * (0 / 3 + (frame_i+100) / total_frames))
    img[width/3:width*2/3, :, 1] = 0.5 + 0.5 * np.sin(2 * np.pi * (1 / 3 + (frame_i+100) / total_frames))
    img[width/3:width*2/3, :, 2] = 0.5 + 0.5 * np.sin(2 * np.pi * (2 / 3 + (frame_i+100) / total_frames))
    img[width*2/3:width, :, 0] = 0.5 + 0.5 * np.sin(2 * np.pi * (0 / 3 + (frame_i+200) / total_frames))
    img[width*2/3:width, :, 1] = 0.5 + 0.5 * np.sin(2 * np.pi * (1 / 3 + (frame_i+200) / total_frames))
    img[width*2/3:width, :, 2] = 0.5 + 0.5 * np.sin(2 * np.pi * (2 / 3 + (frame_i+200) / total_frames))

    img = np.round(255 * img).astype(np.uint8)
    img = np.clip(img, 0, 255)

    frame = av.VideoFrame.from_ndarray(img, format='rgb24')
    packet = stream.encode(frame)

    if packet:
        out.mux(packet)
        if somevar%100 == 0 :print "packet muxing yet..."
print img
print("muxing complete; packet muxed - {}".format(somevar))
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
