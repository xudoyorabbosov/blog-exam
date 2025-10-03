
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True)
    created_at = Column(DateTime,server_default=func.now())
       

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    user_id =Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime,server_default=func.now())

    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(String, niullable = False)
    post_id = Column(Integer, ForeignKey('posts.id'),nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
  
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
