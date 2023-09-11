"""  
SQLAlchemy ORM = Object relational Mapper (объектно-реляционное отображение), технология для работы с БД с помощью ООП
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, PrimaryKeyConstraint, UniqueConstraint, ForeignKeyConstraint, Index
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from sqlalchemy.orm.session import sessionmaker, Session


database = 'postgresql://aktanbro2010:1@localhost:5432/sql_alchemy'
db = create_engine(database)


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(40), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(30), nullable=False)
    posts = relationship('Post', backref='author')
    
    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('username'),
        UniqueConstraint('email')
    )


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    slug = Column(String(20), nullable=False)
    content = Column(String(250), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())
    author_id = Column(Integer, ForeignKey('users.id'))

    __table_args__ = (
        ForeignKeyConstraint(['author_id'], ['users.id']),
        Index('title_content_index', 'title', 'content')
    )


# Base.metadata.create_all(db)
# drop_all - удалить все таблицы

# создание соединения с БД
Session = sessionmaker(db)

# Открытие соединения
session = Session()

# user1 = User(
#     username = 'test_user3', 
#     email = 'test3@gmail.com', 
#     password = 'superpassword'
# )

# user2 = User(
#     username = 'test_user4', 
#     email = 'test4@gmail.com', 
#     password = 'superpassword'
# )

# print(user1.email, user2.username)

# session.add(user1)
# session.add(user2)
# session.add_all([user1, user2])

# session.commit()


# print(session.query(User).all())

# user = session.query(User).get(1)
# print(user, user.email)

# post1 = Post(
#     title = 'first post',
#     slug = 'first',
#     content = 'test post',
#     author_id = user.id
# )

# user = session.query(User).filter(User.username == 'test_user').all()

# print(user[0].username)

# SELECT * FROM users WHERE username == 'test_user';

# session.add(post1)
# session.commit()


user = session.query(User).get(3)
# session.delete(user)
# session.commit()
user.email = 'test6@gmail.com'
user.username = 'test_user6'
session.add(user)
session.commit()