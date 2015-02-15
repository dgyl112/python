#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
sqlite3 查询
'''
import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 占位符 ?
# cursor.execute('select * from user where id=?', '1')
cursor.execute('select * from user')

# 获得查询结果集:
values = cursor.fetchall()
# [(1, u'Michael'), (2, u'Michael')]
print values

cursor.close()
conn.close()