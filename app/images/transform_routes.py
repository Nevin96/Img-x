import os
from uuid import uuid4
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.auth.deps import get_current_user
from app.models.image import Image
from app.models.image_variant import ImageVariant
from app.images.service import create_thumbnail,resize_image,convert_format

router = APIRouter(prefix="/images",tags=["transform"])

@router.post("/{image_id}/resize")
def resize(
    image_id : int,
    width : int,
    height : int,
    user_id : str = Depends(get_current_user),
    db : Session = Depends(get_db)
):
    image = db.query(Image).filter(Image.id == image_id,Image.owner_id == int(user_id)).first()
    if not image:
        raise HTTPException(404,"image not found!")
    
    new_name = f"{uuid4()}.jpg"
    output_path = f"media/variants/{new_name}"

    resize_image(image.file_path,output_path,width,height)

    variant = ImageVariant(
        image_id = image.id,
        file_path = output_path,
        width = width,
        height = height,
        format = "JPEG",
        variant_type = "resized"
    )
    db.add(variant)
    db.commit()

    return {"message" : "resized", "path" : output_path}

@router.post("/{images_id}/thumbnail")
def thumbnail(
    image_id : int,
    user_id : str = Depends(get_current_user),
    db : Session = Depends(get_db)
):
    image = db.query(Image).filter(Image.id == image_id,Image.owner_id == int(user_id)).first()
    if not image: 
        raise HTTPException(404,"image not found!")
    
    new_name = f"{uuid4()}.jpg"
    output_path = f"media/variants/{new_name}"
    create_thumbnail(image.file_path,output_path)
    variant = ImageVariant(
        image_id = image.id,
        file_path = output_path,
        width = 200,
        height = 200,
        format = "JPEG",
        variant_type = "thumbnail"
    )
    db.add(variant)
    db.commit()

    return {"message" : 'thumbnail created','path' : output_path}
