from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.responses import JSONResponse
from model import RetinalInferenceEngine
from utils import validate_image_upload
import time

app = FastAPI(title="Retinal Screening API - Core Implementation")

# Initialize modular inference engine instance
inference_engine = RetinalInferenceEngine("yolov8n.pt")

@app.post("/predict/")
async def predict_anomaly(
    file: UploadFile = File(...)
):
    start_time = time.time()
    
    # Read file bytes for validation and processing
    image_bytes = await file.read()
    
    # Apply input validation (Stage 2 / NFR-02)
    validate_image_upload(file.content_type, len(image_bytes))
    
    try:
        # Run inference via modular engine (Default threshold 0.25)
        detections = inference_engine.predict(image_bytes, confidence_threshold=0.25)
        
        processing_time = round(time.time() - start_time, 3)
        
        return JSONResponse(content={
            "status": "success",
            "filename": file.filename,
            "processing_time_seconds": processing_time,
            "detections_count": len(detections),
            "detections": detections
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))