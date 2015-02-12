#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
正则表达式
@author: lee
'''

import re
# 强烈建议使用Python的r前缀，就不用考虑转义的问题
print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')    # <_sre.SRE_Match object at 0x0000000001F1D5E0>
print re.match(r'^\d{3}\-\d{3,8}$', '010 12345')    # None

'''
\d可以匹配一个数字，\w可以匹配一个字母或数字
.可以匹配任意字符
*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符

[]表示范围
[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等
[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量
[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）

A|B可以匹配A或B，所以[P|p]ython可以匹配'Python'或者'python'

^表示行的开头，^\d表示必须以数字开头
$表示行的结束，\d$表示必须以数字结束
py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'
'''


'''
切分字符串
'''
print 'a b   c'.split(' ')                  # ['a', 'b', '', '', 'c']
print re.split(r'\s+', 'a b   c')           # ['a', 'b', 'c']
print re.split(r'[\s\,]+', 'a,b, c  d')     # ['a', 'b', 'c', 'd']
print re.split(r'[\s\,\;]+', 'a,b;; c  d')  # ['a', 'b', 'c', 'd']



'''
分组
用()表示的就是要提取的分组（Group）。

如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
'''
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group(0)            # 010-12345
print m.groups()            # ('010', '12345')


t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print m.group(0)            # 19:05:30
print m.groups()            # ('19', '05', '30')

'''
贪婪匹配
正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
'''
print re.match(r'^(\d+)(0*)$', '102300').groups()           # ('102300', '')
# 加个?就可以让\d+采用非贪婪匹配
print re.match(r'^(\d+?)(0*)$', '102300').groups()          # ('1023', '00')
print re.match(r'^(\d+?)(0*)$', '1023050').groups()         # ('102305', '0')


'''
编译
如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式.
'''
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()              # ('010', '12345')
print re_telephone.match('010-8086').groups()               # ('010', '8086')



mail = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
m = re.match(mail, r'sdfs@vdfv.com')            # <_sre.SRE_Match object at 0x00000000020136B8>
print m.group(0), m.groups()                    # sdfs@vdfv.com (None, None, '.com')







