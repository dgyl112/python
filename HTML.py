#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
HTML
HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。

好在Python提供了HTMLParser来非常方便地解析HTML.

feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
'''
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!--%s-->' % data)

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html><head></head><body><p>Some <a href=\"#\">html</a>
<!-- 注释 --> &nbsp; &#1234; tutorial...<br>END</p></body></html>''')


'''
<html>
<head>
</head>
<body>
<p>
data
<a>
data
</a>
data
<!-- 注释 -->
data
&nbsp;
data
&#1234;
data
<br>
data
</p>
</body>
</html>
'''