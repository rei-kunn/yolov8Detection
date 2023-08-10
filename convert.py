from ultralytics import YOLO

model = YOLO('best.pt')
model.export(format='saved_model')