from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 创建数据库ORM对象
db = SQLAlchemy()

# 创建基类,普通数据表类继承该基类
class Base(db.Model):

    # 不将该表当作Model类
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow, onupdate=datetime.utcnow)

# 创建数据库表结构
class User(Base):
    __tablename__ = 'user'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False, index=True)
