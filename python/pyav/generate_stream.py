import av

file1=av.open('out.mp4', 'r')
file2=av.open('81307.mp4', 'r')

out = av.open("rtmp://172.30.120.246:1935/myapp/pythonstream", mode='w')

stream = out.add_stream('libx264', rate=fps)
stream.width = 1280
stream.height = 720
stream.pix_fmt = 'yuv420p'


