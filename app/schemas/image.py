from pydantic import BaseModel
from typing import List

class ImageResponse(BaseModel):
    id: int
    filename : str
    width : int
    height : int
    format : str
    size_bytes : int

    class Config:
        from_attributes = True

class PaginatedImages(BaseModel):
    total : int
    page : int
    limit : int
    items : List[ImageResponse]