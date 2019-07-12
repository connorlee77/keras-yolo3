import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import matplotlib.pyplot as plt


yolo = YOLO()


input_path = 'input/'
output_path = 'output/'
filename = 'porsche.jpg'
image = Image.open(input_path + filename).convert("RGB")
r_image = yolo.detect_image(image)
plt.figure()
plt.imshow(r_image)
plt.show()


yolo.close_session()