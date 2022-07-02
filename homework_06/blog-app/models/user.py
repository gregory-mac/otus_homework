from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from .database import db


class User(db.Model):
    name = Column(String(50), nullable=False, unique=False)
    username = Column(String(20), nullable=False, unique=True, primary_key=True)
    email = Column(String(30), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user")
