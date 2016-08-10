# -*- coding:utf-8 -*-

import optparse

charsets = ['ascii', 'utf-8', 'gbk', 'utf-16-le', 'utf-16-be']

# 返回文件filename的编码,如果找不到编码，返回'binary'
def detect(filename):
    result = 'binary'
    content = open(filename, 'r').read()
    for charset in charsets:
        try:
            content.decode(charset)
            result = charset
            break
        except:
            pass

    return result



if __name__ == '__main__':
    parser = optparse.OptionParser("%prog file1 [file2 ...]")

    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.print_help()
        exit(1)

    (options, args) = parser.parse_args()

    for arg in args:
        charset = detect(arg)
        if charset != 'binary':
            print arg, ':', detect(arg), 'text file'
        else:
            print arg, ':', detect(arg), 'file'

