import json
from database import Base, engine, SessionLocal
from models import User, Post, Comment

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def load_demo_data():
    db = SessionLocal()
    with open("demo_data.json", "r") as f:
        data = json.load(f)

    # Users larni kriting
    db.commit()

    # Posts larni kriting
    db.commit()

    # Comments larni kriting
    db.commit()

    db.close()

if __name__ == "__main__":
    init_db()
    load_demo_data()
    print("✅ Database initialized and demo data loaded!")
