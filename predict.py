import os

from ultralytics import YOLO

yolo = YOLO('runs/detect/train18/weights/best.pt', task='detect')

for i in os.listdir('datasets/bvn/images/train'):
    result = yolo(source='datasets/bvn/images/train/'+i, save=True)

