from sqlalchemy.orm import Session
from models import User, Post, Comment

# CRUD
def create_user(db: Session, username: str, email: str):
    pass

def create_post(db: Session, user_id: int, title: str, body: str):
    pass

def create_comment(db: Session, user_id: int, post_id: int, text: str):
    pass

def update_post(db: Session, post_id: int, title: str, body: str):
    pass

def delete_post(db: Session, post_id: int):
    pass


# Queries
def get_user_posts(db: Session, user_id: int):
    pass

def get_post_comment_count(db: Session, post_id: int):
    pass

def get_latest_posts(db: Session, limit: int = 5):
    pass

def search_posts_by_title(db: Session, keyword: str):
    pass

def paginate_posts(db: Session, page: int = 1, per_page: int = 5):
    pass
