from fastapi import HTTPException

def validate_image_upload(content_type: str, file_size: int):
    if file_size == 0:
        raise HTTPException(
            status_code=400,
            detail="File is empty."
        )
    # Validate MIME type (NFR-02)
    if not content_type or not content_type.startswith("image/"):
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Only image files (JPEG, PNG) are allowed."
        )
    # File size limit (max 10MB)
    if file_size > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds the 10MB maximum."
        )