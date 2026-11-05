from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI(title="Retinal Screening API Prototype")

# Loading the base YOLOv8 model (using CPU for local Mac implementation)
model = YOLO("yolov8n.pt")

@app.post("/predict/")
async def predict_anomaly(file: UploadFile = File(...)):
    # Ensure te file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")
    
    try:
        # Reading image bytes
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        results = model(image)
        
        # Viewing the bounding boxes
        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Format: [x_center, y_center, width, height]
                coords = box.xywh[0].tolist()
                confidence = float(box.conf[0])
                detections.append({
                    "bounding_box": coords,
                    "confidence": round(confidence, 2)
                })
                
        return JSONResponse(content={"status": "success", "detections": detections})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))