#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年1月4日

@author: lee
'''

import os
from os import path

def renameUrlimage2jpg(dirPath):
    if path.exists(dirPath) and path.isdir(dirPath) :
        os.chdir(dirPath)
    else:
        return
    for oldFileName in os.listdir(dirPath):
        nPos = oldFileName.find('.urlimage')
        if ( nPos == len(oldFileName) - 9 ) :
            os.rename( oldFileName, oldFileName + '.jpg')

def main():
    renameUrlimage2jpg('''C:\\Users\\lee\\Desktop\\urlimage''')

if __name__ == '__main__':
    main()