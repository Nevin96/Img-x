import os 
from uuid import uuid4
from fastapi import APIRouter,Depends,HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db.deps import get_db
from app.auth.deps import get_current_user
from app.models.image import Image
from app.models.image_variant import ImageVariant
from app.images.service import resize_image

router = APIRouter(prefix="/images",tags=['dynamic'])
@router.get("/{image_id}")
def dynamic_router(
    image_id : int,
    w : int | None = None,
    h : int | None = None,
    user_id : str = Depends(get_current_user),
    db : Session = Depends(get_db)
):
    image = db.query(Image).filter(Image.id == image_id).first()
    if not image:
        raise HTTPException(404,"Image not found")
    if not w and not h:
        return FileResponse(image.file_path)
    variant = db.query(ImageVariant).filter(ImageVariant.image_id == image_id,
                                            ImageVariant.width == w,
                                            ImageVariant.height == h).first()
    if variant:
        return FileResponse(variant.file_path)
    
    new_name = f"{uuid4()}.jpg"
    output_path = f"media/variants/{new_name}"
    resize_image(image.file_path,output_path,w,h)
    try:
        variant = ImageVariant(
            image_id = image_id,
            file_path = output_path,
            width = w,
            height = h,
            format = 'JPEG',
            variant_type = 'dynamic'
        )
        db.add(variant)
        db.commit()
    except IntegrityError:
        db.rollback()
        variant = db.query(ImageVariant).filter(
            ImageVariant.image_id == image_id,
            ImageVariant.height == h,
            ImageVariant.width == w,
            ImageVariant.format == "JPEG"
        ).first()
    return FileResponse(variant.file_path)