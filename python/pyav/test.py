import av
import sys
from PIL import Image 
from PIL import ImageDraw
from PIL import ImageFont
import logging
font = ImageFont.truetype("Helvetica.ttf",80)
logging.basicConfig(level=logging.DEBUG)

w,h=1920,1080
out=av.open("test.mov",mode="w",options={"preset":"fast", "crf":"22"})
stream = out.add_stream('libx264', 24)
stream.width = w
stream.height = h
stream.pix_fmt = "yuv420p"
idx = 0
for frame in range(64):
        image = Image.new('RGB', (w, h))
        outframe = av.VideoFrame(w,h, 'rgb24')
        draw=ImageDraw.Draw(image)
        draw.text((10+4*idx,10+4*idx), "Hello", font=font, fill=(0,255,255,255))
        outframe.planes[0].update_from_string(image.tobytes())
	outframe.pts = None
        packet = stream.encode(outframe)
        if packet:
            out.mux(packet)
        idx += 1
    
while True:
    out_packet = stream.encode()
    if out_packet:
        out.mux(out_packet)
    else:
        break
out.close()
