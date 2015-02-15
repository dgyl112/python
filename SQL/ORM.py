#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sqlalchemy
'''
# 导入:
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(20))

# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
# engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
engine = create_engine('sqlite:///test.db',echo=True)  

print engine
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

'''
插入
前提是有这样的表
'''
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()


'''
查询
'''
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
try:
    user = session.query(User).filter(User.id==7).one()
    
    # 打印类型和对象的name属性:
    print 'type:', type(user)           # type: <class '__main__.User'>
    print 'name:', user.name            # name: Bob
except:
    print 'query dabase error'

# 关闭Session:
session.close()

'''
一对多、多对多
关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
'''
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class User2(Base):
    __tablename__ = 'user2'

    id = Column(Integer, primary_key=True,autoincrement = True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的
    user_id = Column(String(20), ForeignKey('user2.id'))
