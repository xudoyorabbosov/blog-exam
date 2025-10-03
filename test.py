from database import SessionLocal
from crud import (
    create_user, create_post, create_comment, update_post, delete_post,
    get_user_posts, get_post_comment_count, get_latest_posts,
    search_posts_by_title, paginate_posts
)
from models import User, Post, Comment

def run_tests():
    db = SessionLocal()
    try:
        print("--- CRUD va Query funksiyalarini tekshirish ---")

        print("\n1. Yangi user yaratish...")
        new_user = create_user(db, "test_user", "test@example.com")
        print(f"Yangi user yaratildi: {new_user.username}")

        print("\n2. Yangi post yaratish...")
        new_post = create_post(db, new_user.id, "Test Post", "Bu test uchun yozilgan post.")
        print(f"Yangi post yaratildi: {new_post.title}")

        print("\n3. Yangi comment yaratish...")
        new_comment = create_comment(db, new_user.id, new_post.id, "Ajoyib post!")
        print(f"Yangi comment yaratildi: {new_comment.text}")

        print("\n4. Postni yangilash...")
        updated_post = update_post(db, new_post.id, "Yangilangan Test Post", "Yangi yangilangan matn.")
        if updated_post:
            print(f"Post yangilandi: {updated_post.title}")

        print("\n5. User postlarini olish...")
        user_posts = get_user_posts(db, new_user.id)
        print(f"{new_user.username}ning postlari soni: {len(user_posts)}")

        print("\n6. Post commentlari sonini hisoblash...")
        comment_count = get_post_comment_count(db, new_post.id)
        print(f"'{new_post.title}' uchun commentlar soni: {comment_count}")

        print("\n7. Oxirgi 3 ta postni olish...")
        latest_posts = get_latest_posts(db, limit=3)
        for post in latest_posts:
            print(f" - {post.title}")

        print("\n8. Postlarni 'test' so'zi bo'yicha qidirish...")
        search_results = search_posts_by_title(db, "test")
        for post in search_results:
            print(f" - {post.title}")

        print("\n9. Postlarni sahifalash (2-sahifa, har sahifada 2 ta)...")
        paginated_posts = paginate_posts(db, page=2, per_page=2)
        for post in paginated_posts:
            print(f" - {post.title}")

        print("\n10. Test postini o'chirish...")
        delete_result = delete_post(db, new_post.id)
        print(f"Post o'chirildi: {delete_result}")
        
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        
    finally:
        db.close()

if __name__== "main":
    run_tests()