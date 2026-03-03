import os 
from uuid import uuid4
from fastapi import APIRouter,Depends,HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import BackgroundTasks

from app.db.deps import get_db
from app.auth.deps import get_current_user
from app.models.image import Image
from app.models.image_variant import ImageVariant
from app.images.tasks import process_variant
from app.images.service import resize_image

router = APIRouter(prefix="/images",tags=['dynamic'])
@router.get("/{image_id}")
def dynamic_router(
    image_id : int,
    w : int | None = None,
    h : int | None = None,
    background_tasks : BackgroundTasks = BackgroundTasks(),
    db : Session = Depends(get_db)
):
    image = db.query(Image).filter(Image.id == image_id).first()
    if not image:
        raise HTTPException(404,"Image not found")
    if not w and not h:
        return FileResponse(image.file_path)
    variant = db.query(ImageVariant).filter(ImageVariant.image_id == image_id,
                                            ImageVariant.width == w,
                                            ImageVariant.height == h,
                                            ImageVariant.format == "JPEG").first()
    if variant:
        return FileResponse(variant.file_path)
    
    new_name = f"{image_id}_{w}x{h}.jpg"
    output_path = f"media/variants/{new_name}"
    if os.path.exists(output_path):
        return FileResponse(output_path)
    
    background_tasks.add_task(
        process_variant,
        image_id,
        image.file_path,
        output_path,
        w,
        h
    )
    return {
        "status": "processing",
        "retry_url" : f"/images/{image_id}?w={w}&h={h}"
    }