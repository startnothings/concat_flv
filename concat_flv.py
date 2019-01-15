# coding=utf-8
"""
需要先将fmpeg.exe路径加入环境变量，或者把ffmpeg.exe和视频放在一起
再将本脚本放在视频目录下运行
"""
import os
import codecs
import re
import sys

# 获取flv文件
file_list = os.listdir(os.path.dirname(__file__))
flv_list = []
pattern = re.compile('.*\.flv$')

for item in file_list:
    if os.path.isfile(item) and pattern.match(item):
        if sys.version < '3':
            item = item.decode('gbk')
        flv_list.append(item)

# 生成txt
with codecs.open('mylist.txt', 'w', 'utf8') as f:
    for flv in flv_list:
        f.write(u"file '%s'\r\n" % flv)

# 执行转换命令
os.system('ffmpeg -f concat -safe 0 -i mylist.txt -c copy all.flv')

# 删除txt
os.remove('mylist.txt')

# 结束
os.system('pause')

