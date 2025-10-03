# 📝 Exam – Blog Application

## **Model requirements**

1. `User`

   * id (PK)
   * username (unique, not null)
   * email
   * created_at

2. `Post`

   * id (PK)
   * title
   * body
   * user_id (FK → users.id)
   * created_at

3. `Comment`

   * id (PK)
   * text
   * post_id (FK → posts.id)
   * user_id (FK → users.id)
   * created_at

**ORM relationshiplari (majburiy):**

* `User.posts` → one-to-many
* `User.comments` → one-to-many
* `Post.comments` → one-to-many
* `Comment.user` va `Comment.post` → many-to-one

---

## **Tasks**

### 1. CRUD (asosiy amaliyotlar)

`crud.py` faylida quyidagilarni ORM orqali yozing:

* `create_user(db, username, email)` – yangi user qo‘shish
* `create_post(db, user_id, title, body)` – yangi post yaratish (user_id bilan bog‘liq bo‘lishi shart)
* `create_comment(db, user_id, post_id, text)` – yangi comment yozish
* `update_post(db, post_id, title, body)` – postni yangilash
* `delete_post(db, post_id)` – postni o‘chirish

---

### 2. Query topshiriqlar (ORM bilan yozilishi shart!)

* `get_user_posts(db, user_id)` – berilgan userning barcha postlarini chiqarish
* `get_post_comment_count(db, post_id)` – berilgan post uchun commentlar sonini chiqarish
* `get_latest_posts(db, limit=5)` – oxirgi 5 ta yozilgan postni chiqarish (created_at bo‘yicha tartiblangan)
* `search_posts_by_title(db, keyword)` – postlarni `title` bo‘yicha `ilike` orqali qidirish
* `paginate_posts(db, page=1, per_page=5)` – pagination qilish (1-sahifada 5 ta post chiqsin)

---

## **Imtihon topshirish tartibi**

1. `blog_db` nomli PostgreSQL database yarating.
2. `models.py` da ORM modellari va relationshiplarni to‘g‘ri yozing.
3. `main.py` orqali:

   * Database initialize qiling (`Base.metadata.create_all`)
   * `demo_data.json` fayldan ma’lumotlarni DB ga yuklang
4. `crud.py` faylida yuqoridagi CRUD va Query funksiyalarini yozing.
5. Har bir yozgan funksiyani `test.py` faylda chaqirib tekshiring.
