#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
安装第三方模块
在Python中，安装第三方模块，是通过setuptools这个工具完成的。

PIL (Python Imaging Library)     处理图像的工具库
MySQL-python:                    MySQL的驱动
numpy                            用于科学计算的NumPy库
Jinja2                           用于生成文本的模板工具
'''

'''
PIL
'''
try:
    '''缩放'''
    import Image

    # 打开一个jpg图像文件，注意路径要改成你自己的:
    im = Image.open('test.png')
    # 获得图像尺寸:
    w, h = im.size
    # 缩放到50%:
    im.thumbnail((w//2, h//2))
    # 把缩放后的图像用jpeg格式保存:
    im.save('test_thumbnail.png', 'png')
    
    ''' 模糊化 '''
    import ImageFilter

    im = Image.open('test.png')
    im2 = im.filter(ImageFilter.BLUR)
    im2.save('test_blur.png', 'png')
    
    
except ImportError,e:
    print 'ImportError:',e
except IOError,e:
    print 'IOError:',e                  # IOError: decoder zip not available
    



import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('c:/windows/fonts/arial.ttf', 36)

# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg');