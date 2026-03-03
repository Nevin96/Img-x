import os 
from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from app.models.image_variant import ImageVariant
from app.images.service import resize_image
from sqlalchemy.exc import IntegrityError

def process_variant(image_id : int,input_path : str,output_path: str,h : int,w: int):
    db : Session = SessionLocal()
    try:
        existing = db.query(ImageVariant).filter(
            ImageVariant.image_id == image_id,
            ImageVariant.height == h,
            ImageVariant.width == w,
            ImageVariant.format == "JPEG"
        ).first()
        if existing:
            return
        resize_image(input_path,output_path,w,h)
        variant = ImageVariant(
            image_id = image_id,
            file_path = output_path,
            width = w,
            height = h,
            format = "JPEG",
            variant_type = "dynamic"
        )
        db.add(variant)
        db.commit()
    except IntegrityError:
        db.rollback()
    finally:
        db.close()