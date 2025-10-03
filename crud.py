from sqlalchemy.orm import Session
from sqlalchemy import func
from models import User, Post, Comment


def create_user(db: Session, username: str, email: str):
    db_user = User(username=username, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_post(db: Session, user_id: int, title: str, body: str):
    db_post = Post(user_id=user_id, title=title, body=body)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def create_comment(db: Session, user_id: int, post_id: int, text: str):
    db_comment = Comment(user_id=user_id, post_id=post_id, text=text)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def update_post(db: Session, post_id: int, title: str, body: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post: 
        post.title = title
        post.body = body 
        db.commit()
        db.refresh(post)
        return post
    return None

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False

def get_user_posts(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user.posts
    return []

def get_post_comment_count(db: Session, post_id: int):
    count = db.query(Comment).filter(Comment.post_id == post_id).count()
    return count

def get_latest_posts(db: Session, limit: int = 5):
    return db.query(Post).order_by(Post.created_at.desc()).limit(limit).all()

def search_posts_by_title(db: Session, keyword: str):
    return db.query(Post).filter(Post.title.ilike(f"%{keyword}%")).all()

def paginate_posts(db: Session, page: int = 1, per_page: int = 5):
    offset = (page -1) * per_page
    return db.query(Post).offset(offset).limit(per_page).all()
