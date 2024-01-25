from ultralytics import YOLO
import os
from hyperparams import *

model = YOLO(model_yolo)

results = model.train(data=os.path.join(DATA_PATH, 'data.yaml'), epochs=EPOCHS, batch=BATCH, name='yolo8')
