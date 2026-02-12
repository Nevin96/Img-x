import os 
from uuid import uuid4

from fastapi import APIRouter,UploadFile,HTTPException,Depends,File
from sqlalchemy.orm import Session
from PIL import Image as PILImage

from app.db.deps import get_db
from app.models.image import Image
from app.schemas.image import ImageResponse
from app.auth.deps import get_current_user

router = APIRouter(prefix='/images',tags=['image'])

UPLOAD_DIR = "media/images"
os.makedirs(UPLOAD_DIR,exist_ok=True)

@router.post('/upload',response_model=ImageResponse)
def upload_image(
    file : UploadFile = File(...),
    user_id : str = Depends(get_current_user),
    db : Session = Depends(get_db)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400,detail='invalid image type')
    ext = file.filename.strip('.')[-1]
    filename = f"{uuid4()}.{ext}"
    file_path = os.path.join(UPLOAD_DIR,filename)

    with open(file_path,'wb') as buffer:
        buffer.write(file.file.read())
    
    with PILImage.open(file_path) as img:
        width,height = img.size
        format = img.format
    
    size_bytes = os.path.getsize(file_path)
    image = Image(
        filename = filename,
        file_path = file_path,
        width = width,
        height = height,
        format = format,
        size_bytes = size_bytes,
        owner_id = int(user_id)
    )
    db.add(image)
    db.commit()
    db.refresh(image)

    return image