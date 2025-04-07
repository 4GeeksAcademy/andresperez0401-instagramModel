from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

# ------------------- USER -----------------------


class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    posts: Mapped[list["Post"]] = relationship(
        'Post', back_populates='author', lazy=True)
    comments: Mapped[list["Comment"]] = relationship(
        'Comment', back_populates='user', lazy=True)
    likes: Mapped[list["Like"]] = relationship(
        'Like', back_populates='user', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # No incluyas la contraseña nunca en un serialize
        }

# -------------------- POST ----------------------------


class Post(db.Model):
    __tablename__ = 'post'

    id_post: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(250), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)

    comments: Mapped[list["Comment"]] = relationship(
        'Comment', back_populates='post', lazy=True)
    likes: Mapped[list["Like"]] = relationship(
        'Like', back_populates='post', lazy=True)

    def serialize(self):
        return {
            "id_post": self.id_post,
            "content": self.content,
            "author_id": self.user_id
        }

# ---------------------- LIKE -----------------------


class Like(db.Model):
    __tablename__ = 'like'

    id_like: Mapped[int] = mapped_column(primary_key=True)
    id_post: Mapped[int] = mapped_column(
        ForeignKey('post.id_post'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)

# ------------------------ COMMENT ----------------------------


class Comment(db.Model):
    __tablename__ = 'comment'

    id_comment: Mapped[int] = mapped_column(primary_key=True)
    comentario: Mapped[str] = mapped_column(String(300), nullable=False)

    id_post: Mapped[int] = mapped_column(
        ForeignKey('post.id_post'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)

    def serialize(self):
        return {
            "id_comment": self.id_comment,
            "comentario": self.comentario,
            "id_post": self.id_post,
            "user_id": self.user_id
        }
