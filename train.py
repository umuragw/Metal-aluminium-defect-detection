from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.train(data='my_data.yaml', workers=0, epochs=100, batch=32, imgsz=640, device=0)
