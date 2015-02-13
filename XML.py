#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
SAX

当SAX解析器读到一个节点时：
<a href="/">python</a>
会产生3个事件：
start_element事件，在读取<a href="/">时；
char_data事件，在读取python时；
end_element事件，在读取</a>时。
'''
from xml.parsers.expat import ParserCreate
from pip._vendor.html5lib.treebuilders import dom

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


'''
最简单也是最有效的生成XML的方法是拼接字符串
'''
def encode(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode(r'some & data'))
L.append(r'</root>')
print L                         # ['<?xml version="1.0"?>', '<root>', 'some &amp; data', '</root>']
print ''.join(L)                # <?xml version="1.0"?><root>some &amp; data</root>

'''
DOM
创建一个xml文档
'''
from xml.dom import minidom
 
doc = minidom.Document()
doc.appendChild(doc.createComment("This is a simple xml."))
booklist = doc.createElement("booklist")
doc.appendChild(booklist)
 
def addBook(newbook):
    book = doc.createElement("book")
    book.setAttribute("id", newbook["id"])
     
    title = doc.createElement("title")
    title.appendChild(doc.createTextNode(newbook["title"]))
    book.appendChild(title)
     
    author = doc.createElement("author")
    name = doc.createElement("name")
    firstname = doc.createElement("firstname")
    firstname.appendChild(doc.createTextNode(newbook["firstname"]))
    lastname = doc.createElement("lastname")
    lastname.appendChild(doc.createTextNode(newbook["lastname"]))
    name.appendChild(firstname)
    name.appendChild(lastname)
    author.appendChild(name)
    book.appendChild(author)
     
    pubdate = doc.createElement("pubdate")
    pubdate.appendChild(doc.createTextNode(newbook["pubdate"]))
    book.appendChild(pubdate)
     
    booklist.appendChild(book)
 
addBook({"id":"1001","title":"An apple","firstname":"Peter","lastname":"Zhang","pubdate":"2012-1-12"})
addBook({"id":"1002","title":"Love","firstname":"Mike","lastname":"Li","pubdate":"2012-1-10"})
addBook({"id":"1003","title":"Steve.Jobs","firstname":"Tom","lastname":"Wang","pubdate":"2012-1-19"})
addBook({"id":"1004","title":"Harry Potter","firstname":"Peter","lastname":"Chen","pubdate":"2012-11-11"})

f = file("book.xml","w")
doc.writexml(f)
f.close()


'''
DOM 解析
'''
from xml.dom import Node
 
class bookscanner(object):
    def __init__(self,doc):
        for child in doc.childNodes :
            if child.nodeType == Node.ELEMENT_NODE \
            and child.tagName == "book" :
                bookid = child.getAttribute("id")
                print "*"*20
                print "Book id : " , bookid
                self.handle_book(child)
                 
    def handle_book(self,node):
        for child in node.childNodes :
            if child.nodeType == Node.ELEMENT_NODE :
                if child.tagName == "title":
                    print "Title : " , self.getText(child.firstChild)
                if child.tagName == "author":
                    self.handle_author(child)
                if child.tagName == "pubdate":
                    print "Pubdate : " , self.getText(child.firstChild)
             
    def getText(self,node):
        if node.nodeType == Node.TEXT_NODE :
            return node.nodeValue
        else:
            return ""
         
    def handle_author(self,node):
        author = node.firstChild
        for child in author.childNodes:
            if child.nodeType == Node.ELEMENT_NODE:
                if child.tagName == "firstname" :
                    print "Firstname : ", self.getText(child.firstChild)
                if child.tagName == "lastname" :
                    print "Lastname : " , self.getText(child.firstChild)
     
     
doc = minidom.parse("book.xml")
for child in doc.childNodes :
    if child.nodeType == Node.COMMENT_NODE:
        print "Conment : " , child.nodeValue
    elif child.nodeType == Node.ELEMENT_NODE:
        bookscanner(child)

'''
Conment :  This is a simple xml.
********************
Book id :  1001
Title :  An apple
Firstname :  Peter
Lastname :  Zhang
Pubdate :  2012-1-12
********************
Book id :  1002
Title :  Love
Firstname :  Mike
Lastname :  Li
Pubdate :  2012-1-10
********************
Book id :  1003
Title :  Steve.Jobs
Firstname :  Tom
Lastname :  Wang
Pubdate :  2012-1-19
********************
Book id :  1004
Title :  Harry Potter
Firstname :  Peter
Lastname :  Chen
Pubdate :  2012-11-11
'''