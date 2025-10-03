
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    # column larni yarating

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    # column larni yarating

    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    # column larni yarating
  
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
