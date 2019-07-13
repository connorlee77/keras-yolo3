import sys
import argparse
from yolo import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import results

def readImage(filepath):
	image = Image.open(filepath).convert("RGB")
	return image

yolo = YOLO()

path_to_input_images = 'input'
path_to_output_images = 'output'
path_to_output_csv = 'csv'

results.detect_images(yolo.detect_image, readImage, path_to_input_images, path_to_output_images, path_to_output_csv, output_PIL=True)

yolo.close_session()