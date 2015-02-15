#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
读文件
Python内置了读写文件的函数，用法和C是兼容的。
'''
try:
    f = open('test.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()

# Python引入了with语句来自动帮我们调用close()方法
with open('test.txt', 'r') as f:
    lines = f.readlines()
    print lines
    for line in lines:
        print(line.strip())     # 把末尾的'\n'删掉


with open('test.png', 'rb') as f:
    print f.read(128)           # 每次最多读取512个字节的内容


import codecs
with codecs.open('gbk.txt', 'r', 'gbk') as f:
    print f.read()              # 中文 “你好” 不进行转码会显示成乱码

'''
写文件
'''
f = open('test.txt', 'w')
f.write('Hello, world!')
f.close()

with open('test.txt', 'w') as f:
    f.write('Hello, world!')


'''
操作文件和目录
'''
import os
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print os.name       
try:
    # uname()函数在Windows上不提供
    print os.uname()
except Exception, e:
    print e


'''
环境变量
'''
# 在操作系统中定义的环境变量，全部保存在os.environ这个dict中
print os.environ
# 获取某个环境变量的值，可以调用os.getenv()函数
print os.getenv('PATH')

'''
操作文件和目录
操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
'''
print os.path.abspath('.')
testdir = os.path.join('/', 'testdir')
print testdir
try:
    os.mkdir(testdir)
    os.rmdir(testdir)
except:
    pass



print os.path.split('/Users/michael/testdir/file.txt')  # ('/Users/michael/testdir', 'file.txt')
# os.path.splitext()可以直接让你得到文件扩展名
print os.path.splitext('/path/to/file.txt')             # ('/path/to/file', '.txt')


# os.rename('test.txt', 'test.py')
# os.remove('test.py')

print [x for x in os.listdir('.') if os.path.isdir(x)]
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']



'''
序列化
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
'''
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件。
dd = pickle.dumps(d)
print 'pickle.loads(dd)',pickle.loads(dd)

f = open('dump.txt', 'wb')
# pickle.dump()直接把对象序列化后写入一个file-like Object
pickle.dump(d, f)
f.close()

with open('dump.txt','r') as f:
    print 'pickle.load(f)',pickle.load(f)



'''
JSON
JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。

JSON类型                        Python类型
{}               dict
[]               list
"string"         'str'或u'unicode'
1234.56          int或float
true/false       True/False
null             None
'''
import json
d = dict(name='Bob', age=20, score=88)
# dumps()方法返回一个str，内容就是标准的JSON
dd = json.dumps(d)
print dd
# {u'age': 20, u'score': 88, u'name': u'Bob'}
d = json.loads(dd)          
print d


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('lisa', 28, 100)
#print(json.dumps(s))            # TypeError: <__main__.Student object at 0x000000000226B6A0> is not JSON serializable

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict))

'''
通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
'''
print(json.dumps(s, default=lambda obj: obj.__dict__))


# 反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))   # <__main__.Student object at 0x000000000211C860>

