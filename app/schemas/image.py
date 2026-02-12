from pydantic import BaseModel

class ImageResponse(BaseModel):
    id: int
    filename : str
    width : int
    height : int
    format : str
    size_bytes : int

    class Config:
        from_attributes = True