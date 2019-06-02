from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

width = 12
height = 4

img = np.empty((width, height, 3))
img[width/3:width*2/3, : , :] = 0.5 + 0.5 * np.sin(2 * np.pi * (1 / 3))
img = np.round(255 * img).astype(np.uint8)
img = np.clip(img, 0, 255)
print img
plt.imshow(img)
plt.show()

