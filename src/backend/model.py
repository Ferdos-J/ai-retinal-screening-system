from ultralytics import YOLO
from PIL import Image
import io

class RetinalInferenceEngine:
    def __init__(self, model_path: str = "yolov8n.pt"):
        # Initialize the YOLOv8 model instance
        self.model = YOLO(model_path)

    def predict(self, image_bytes: bytes, confidence_threshold: float = 0.25):
        # Open image from byte stream
        image = Image.open(io.BytesIO(image_bytes))
        
        # Run inference
        results = self.model(image)
        
        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                conf = float(box.conf[0])
                if conf >= confidence_threshold:
                    coords = box.xywh[0].tolist()
                    detections.append({
                        "bounding_box": coords,
                        "confidence": round(conf, 2),
                        "class_id": int(box.cls[0])
                    })
        return detections