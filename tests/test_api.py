import sys
import os
import io
import time
from PIL import Image
from fastapi.testclient import TestClient

# Add src/backend to Python path so main and utils can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/backend")))

from main import app
from utils import validate_image_upload

client = TestClient(app)

def create_sample_image_bytes(format="JPEG", size=(224, 224)):
    """Helper function to generate a valid in-memory test image."""
    img = Image.new("RGB", size, color=(120, 30, 30))
    buf = io.BytesIO()
    img.save(buf, format=format)
    buf.seek(0)
    return buf

# T01: Normal API Integration Test (FR-01, FR-02)
def test_predict_valid_jpeg_image():
    img_bytes = create_sample_image_bytes("JPEG", (224, 224))
    response = client.post(
        "/predict/",
        files={"file": ("fundus_sample.jpg", img_bytes, "image/jpeg")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "detections" in data
    assert isinstance(data["detections"], list)

# T02: Invalid File Type Rejection (NFR-02)
def test_reject_invalid_pdf_file():
    fake_pdf = io.BytesIO(b"%PDF-1.4 fake document content")
    response = client.post(
        "/predict/",
        files={"file": ("report.pdf", fake_pdf, "application/pdf")}
    )
    assert response.status_code == 400
    assert "Invalid file type" in response.json()["detail"]

# T03: Boundary Test - Oversized File > 10MB (NFR-02)
def test_reject_oversized_file():
    oversized_bytes = io.BytesIO(b"0" * (10 * 1024 * 1024 + 100))
    response = client.post(
        "/predict/",
        files={"file": ("huge_scan.jpg", oversized_bytes, "image/jpeg")}
    )
    assert response.status_code == 400
    assert "10MB" in response.json()["detail"]

# T04: Boundary Test - Empty 0-Byte File (Input Validation)
def test_reject_empty_image_file():
    empty_bytes = io.BytesIO(b"")
    response = client.post(
        "/predict/",
        files={"file": ("empty.jpg", empty_bytes, "image/jpeg")}
    )
    assert response.status_code == 400
    assert "empty" in response.json()["detail"].lower()

# T05: Performance Latency Benchmark (NFR-01: < 5.0 seconds)
def test_inference_latency_under_5_seconds():
    img_bytes = create_sample_image_bytes("JPEG", (224, 224))
    start = time.time()
    response = client.post(
        "/predict/",
        files={"file": ("latency_test.jpg", img_bytes, "image/jpeg")}
    )
    elapsed = time.time() - start
    assert response.status_code == 200
    assert elapsed < 5.0