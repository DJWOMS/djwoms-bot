from random import choice

from aiogram import types

from sqlalchemy import create_engine, Column, Integer, BigInteger, String, Text
from sqlalchemy.orm import declarative_base, Session

from utils.variables import DB_NAME


engine = create_engine(f'sqlite:///{DB_NAME}', echo=False)
Base = declarative_base()

session = Session(bind=engine)


def create_tables():
    """Создание БД и таблиц"""
    Base.metadata.create_all(engine)
    return "Успешное создание БД и таблиц"


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True)
    lang = Column(String)

    def __init__(self, message: types.Message):
        self.message = message

    def __repr__(self):
        return f"<User('{self.id}', '{self.message.from_user.id}')>"

    def add(self):
        """Регистрация пользователя"""
        try:
            user = self.__class__(message=self.message)
            user.user_id = self.message.from_user.id
            user.lang = "ru"
            session.add(user)
            session.commit()
            return self.get()
        except:
            session.rollback()
        finally:
            session.close()

    def get(self, **kwargs):
        """Чтение данных пользователя из таблицы"""
        result: User = None
        if kwargs:
            result = session.query(self.__class__).filter_by(**kwargs).first()
        else:
            result = session.query(self.__class__).filter_by(
                user_id=self.message.from_user.id
            ).first()
        return result

    def update(self, instance):
        """Обновление данных пользователя"""
        try:
            session.add(instance)
            session.commit()
            return instance
        except Exception as e:
            print(e)

    def all(self):
        """Получить список пользователей"""
        return [user for user in session.query(self.__class__).distinct()]


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    name = Column(String)
    text = Column(Text)
    post_id = Column(Integer)

    def __init__(self, message: types.Message):
        self.message = message

    def __repr__(self):
        return f"<Comment('{self.id}', '{self.user_id}', '{self.name}')>"

    def add(self, post_id: int = None):
        """Добавляем комментарий в таблицу"""
        try:
            comment = self.__class__(message=self.message)
            comment.user_id = self.message.from_user.id
            comment.name = self.message.from_user.full_name
            comment.text = self.message.text
            comment.post_id = post_id
            session.add(comment)
            session.commit()
            return self.get(post_id=post_id)
        except:
            session.rollback()
        finally:
            session.close()

    def get(self, **kw):
        """Чтение данных пользователя из таблицы"""
        result: Comment = None
        if kw:
            result = session.query(self.__class__).filter_by(**kw).first()
        else:
            result = [comment for comment in session.query(self.__class__).distinct()]
        return result

    def get_random_user(self, post_id: int = None):
        comments = session.query(self.__class__).filter_by(post_id=post_id).all()
        if comments:
            return choice(comments)
        return []

    def get_text(self, post_id: int = None):
        comment = self.__class__(message=self.message)
        user = comment.get_random_user(post_id=post_id)
        if user:
            return f'<b>🆔UserID:</b> <i>{user.user_id}</i>\n<b>👤Имя:</b> <i>{user.name}</i>\n<b>💬Текст: </b><i>{user.text}</i>'
        else:
            return False
