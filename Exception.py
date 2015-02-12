#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年1月20日

@author: lee
'''

try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'


'''
记录错误
logging
'''
import logging
# 配置
logging.basicConfig(level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        # logging.exception(e)
        logging.error(e)

main()
print 'END'

'''
抛出错误
raise语句如果不带参数，就会把当前错误原样抛出。
'''

'''
断言
启动Python解释器时可以用-O参数来关闭assert
python -O err.py
可以把所有的assert语句当成pass来看。
'''
def foo2(s):
    n = int(s)
    # 表达式n != 0应该是True，否则，后面的代码就会出错。
    assert n != 0, 'n is zero!'
    return 10 / n



'''
pdb
pdb.set_trace()
输入命令l来查看代码
输入命令n可以单步执行代码
任何时候都可以输入命令p 变量名来查看变量
输入命令q结束调试，退出程序
'''


'''
单元测试

单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

编写单元测试，我们需要引入Python自带的unittest模块
以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

运行单元测试
    1. if __name__ == '__main__':
        unittest.main()
    2. 在命令行通过参数-m unittest
'''
class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

d = Dict(a=1, b=2)
print '''d['a']''',d['a']
print 'd.a',d.a


import unittest
class TestDict(unittest.TestCase):
    
    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()














