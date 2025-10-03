from database import SessionLocal
import crud

db = SessionLocal()

# Test: user qo‘shish
user = crud.create_user(db, "test_user", "test@example.com")
print("Created User:", user.username)

# Test: user postlari
posts = crud.get_user_posts(db, user.id)
print("User posts:", posts)

# Qolgan function larni ham shu yerda test qiling
