from sqlalchemy import ForeignKey,String,Integer
from sqlalchemy.orm import mapped_column,Mapped,relationship

from app.db.base import Base

class Image(Base):
    __tablename__ = 'images'

    id : Mapped[int] = mapped_column(primary_key=True)
    filename : Mapped[str] = mapped_column(String,index=True)
    filepath : Mapped[str]
    width : Mapped[int]
    height : Mapped[int]
    format : Mapped[str]
    size_bytes : Mapped[int]
    email_id : Mapped[String] = mapped_column( ForeignKey('users.email',ondelete='CASCADE'))
    owner = relationship('User' ,backref='images')