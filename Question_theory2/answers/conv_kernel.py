import numpy as np
import cv2
import matplotlib.pyplot as plt

height, width = 64, 64

img = cv2.imread("akahara_0001.jpg")
img = cv2.resize(img, (width, height)).astype(np.float32)

np.random.seed(0)

k_channel = 4
k_size = 3
kernels = np.random.normal(0, 0.01, [k_size, k_size, k_channel])

out = np.zeros((height-2, width-2, k_channel), dtype=np.float32)

for y in range(height-2):
    for x in range(width-2):
        for ki in range(k_channel):
            out[y, x, ki] = np.sum(img[y:y+3, x:x+3] * kernels[..., ki])

for i in range(k_channel):
    plt.subplot(1,k_channel,i+1)
    plt.imshow(out[..., i], cmap='gray')

plt.show()
