import xml.dom.minidom 

dom = xml.dom.minidom.parse('HPC发端模型.svg')  #打开svg文档（这里将SVG和脚本放到一个目录）
root = dom.documentElement      #得到文档元素对象
gList = root.getElementsByTagName('g')    #得到所有g标签
pathList = root.getElementsByTagName('path')    #得到所有path标签
rectList = root.getElementsByTagName('rect')    #得到所有rect标签
textList = root.getElementsByTagName('text')    #得到所有text标签

# 设置g
for index in range(len(gList)):
    label = gList[index].getAttribute('inkscape:label')
    if gList[index].hasAttribute('inkscape:label'):
        # id = gList[index].getAttribute('id')
        gList[index].setAttribute('id',label[1:])

# 设置path
for index in range(len(pathList)):
    label = pathList[index].getAttribute('inkscape:label')
    if pathList[index].hasAttribute('inkscape:label'):
        # id = pathList[index].getAttribute('id')
        pathList[index].setAttribute('id',label[1:])

# 设置rect
for index in range(len(rectList)):
    label = rectList[index].getAttribute('inkscape:label')
    if rectList[index].hasAttribute('inkscape:label'):
        # id = rectList[index].getAttribute('id')
        rectList[index].setAttribute('id',label[1:])

# 设置text
for index in range(len(textList)):
    label = textList[index].getAttribute('inkscape:label')
    if textList[index].hasAttribute('inkscape:label'):
        # id = textList[index].getAttribute('id')
        textList[index].setAttribute('id',label[1:])

'''
将文档进行重写，注意文档中内容含有中文的情况
open()函数默认是文本模式打开,也就是ANSII编码
在简体中文系统下，ANSII编码代表 GB2312 编码
'''
with open('HPC发端模型.svg', 'w', encoding='utf-8') as f:
    # 缩进 - 换行 - 编码
    dom.writexml(f, addindent='', encoding='utf-8') 