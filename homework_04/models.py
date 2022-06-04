"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    sessionmaker,
    relationship
)
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession
)


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


async_engine = create_async_engine(PG_CONN_URI)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(bind=async_engine, cls=Base)


Session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


class User(Base):
    name = Column(String(50), nullable=False, unique=False)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(30), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user", uselist=False)


class Post(Base):
    user_id = Column(Integer, nullable=False, unique=True)
    title = Column(String(100), nullable=False, unique=True)
    body = Column(String(500), nullable=False, unique=False)

    user = relationship("User", back_populates="posts", uselist=False)
