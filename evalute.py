from hyperparams import *
from ultralytics import YOLO
from train import os


# model_trained = YOLO('runs/detect/yolo8/weights/best.pt')
model_trained = YOLO('best.pt')

val_results = model_trained.val(data=os.path.join(DATA_PATH, 'data.yaml'), conf=CONF, iou=IOU, split='val')
print(val_results)
