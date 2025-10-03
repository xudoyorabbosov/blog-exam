import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/blog_db")
