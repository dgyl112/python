#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
__future__
__future__模块把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性
'''

from __future__ import unicode_literals
from __future__ import division

# still running on Python 2.7
print '\'xxx\' is unicode?', isinstance('xxx', unicode)         # True
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)       # True
print '\'xxx\' is str?', isinstance('xxx', str)                 # False
print 'b\'xxx\' is str?', isinstance(b'xxx', str)               # True


print '10 / 3 =', 10 / 3            # 3.33333333333
print '10.0 / 3 =', 10.0 / 3        # 3.33333333333
print '10 // 3 =', 10 // 3          # 3