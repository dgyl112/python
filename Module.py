#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
任何模块代码的第一个字符串都被视为模块的文档注释
使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名
'''

__author__ = 'lee'

import sys

def test():
    '''
    sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    '''
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

'''
当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
'''
if __name__=='__main__':
    test()
    
    
'''
别名
导入模块时，还可以使用别名，这样，可以在运行时根据当前环境选择最合适的模块。
比如Python标准库一般会提供StringIO和cStringIO两个库，这两个库的接口和功能是一样的，但是cStringIO是C写的，速度更快。
'''
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
    
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5

'''
作用域
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，
__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

Python并没有一种方法可以完全限制访问private函数或变量
'''

# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)



'''
模块搜索路径

默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中

要添加自己的搜索目录，有两种方法：
1. 直接修改sys.path    (在运行时修改，运行结束后失效)
        import sys
        sys.path.append('/Users/michael/my_py_scripts')
2. 设置环境变量PYTHONPATH
                    设置方式与设置Path环境变量类似
                    当导入一个模块时，python解释器先把*.py文件编译成*.pyc，然后在从*.pyc里面导出 (更新py文件必须删除pyc文件)
'''
