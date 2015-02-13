#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Base64
Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

@author: lee
'''

import base64
print base64.b64encode('binary\x00string')          # YmluYXJ5AHN0cmluZw==
print base64.b64decode('YmluYXJ5AHN0cmluZw==')      # 

'''
标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
'''
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')             # abcd++//
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')     # abcd--__
print base64.urlsafe_b64decode('abcd--__')

'''
由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉

标准Base64:
'abcd' -> 'YWJjZA=='
自动去掉=:
'abcd' -> 'YWJjZA'
'''
