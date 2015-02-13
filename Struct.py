#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
struct
解决str和其他二进制数据类型的转换

@author: lee
'''
import struct
'''
pack函数把任意数据类型变成字符串
pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
'''
print struct.pack('>I', 10240099)       # '\x00\x9c@c'

'''
unpack把str变成相应的数据类型
根据>IH的说明，后面的str依次变为I：4字节无符号整数和H：2字节无符号整数。
'''
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')      # (4042322160L, 32896)

'''
BMP 前30个字节
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图； 一个4字节整数：表示位图大小； 
一个4字节整数：保留位，始终为0； 一个4字节整数：实际图像的偏移量； 
一个4字节整数：Header的字节数； 一个4字节整数：图像宽度； 一个4字节整数：图像高度； 
一个2字节整数：始终为1； 一个2字节整数：颜色数。
'''

# 最后一个 \ 表示下一行与本行为同一行
s = '''\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\
\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'''
print struct.unpack('<ccIIIIIIHH', s)       # ('B', 'M', 691256, 0, 54, 40, 640, 360, 1, 24)


'''
Format       C Type                  Python type            Standard size    Notes
x            pad byte                no value          
c            char                    string of length 1         1     
b            signed char             integer                    1            (3)
B            unsigned char           integer                    1            (3)
?            _Bool                   bool                       1            (1)
h            short                   integer                    2            (3)
H            unsigned short          integer                    2            (3)
i            int                     integer                    4            (3)
I            unsigned int            integer                    4            (3)
l            long                    integer                    4            (3)
L            unsigned long           integer                    4            (3)
q            long long               integer                    8            (2), (3)
Q            unsigned long long      integer                    8            (2), (3)
f            float                   float                      4            (4)
d            double                  float                      8            (4)
s            char[]                  string          
p            char[]                  string          
P            void *                  integer                                 (5), (3)
'''