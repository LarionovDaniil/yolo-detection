from evalute import *
from functions import *
from PIL import Image
from train import os

num = 0
orig = []
predicted = []

for photo in os.listdir('/kaggle/input/one-class-pole/valid/images'):
    results = model_trained.predict('/kaggle/input/one-class-pole/valid/images/' + photo, conf=0.3, iou=0.3)
    result = results[0]
    if len(result.boxes.conf) > orig_count_boxes(photo):
        orig.append(photo)
        predicted.append(result.plot()[:, :, ::-1])


Image.fromarray(draw_orig(orig[num]))
Image.fromarray(predicted[num])
