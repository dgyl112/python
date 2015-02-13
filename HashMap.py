#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
hashlib
哈希算法又称摘要算法、散列算法。

提供了常见的摘要算法，如MD5，SHA1等等。
它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），
只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
'''

'''
MD5
MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
'''
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()                       # d26a53750bc40b38b65a520292f69306

# 如果数据量很大，可以分块多次调用update()
md5 = hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest()                       # d26a53750bc40b38b65a520292f69306


'''
SHA1
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
'''
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()                      # 2c76b57293ce30acef38d98f6046927161b46a44

'''
SHA256

比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。
'''
sha256 = hashlib.sha256()
sha256.update('how to use sha1 in ')
sha256.update('python hashlib?')
print sha256.hexdigest()                    # 17cc523c8f5550ea172a5254221d99576249d91b61dedecdf49b4827c7896fbf
