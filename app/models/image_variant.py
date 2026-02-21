from sqlalchemy import ForeignKey,String,Integer
from sqlalchemy.orm import Mapped,mapped_column,relationship

from app.db.base import Base

class ImageVariant(Base):
    __tablename__ = "image_variants"

    id : Mapped[int] = mapped_column(primary_key=True)
    image_id : Mapped[int] = mapped_column(ForeignKey("images.id",ondelete="CASCADE"))
    file_path : Mapped[str]
    width : Mapped[int]
    height : Mapped[int]
    format : Mapped[str]
    variant_type : Mapped[str]

    image = relationship("Image",backref="variants")