#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
UDP 服务端
'''
import socket
# SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
# 不需要调用listen()

print 'Bind UDP on 9999...'
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print 'Received from %s:%s.' % addr
    # 注意这里省掉了多线程
    s.sendto('Hello, %s!' % data, addr)
