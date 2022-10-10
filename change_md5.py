'''
Descripttion: 
version: 
Author: qiuxchao
Date: 2022-04-22 13:43:34
LastEditors: qiuxchao
LastEditTime: 2022-04-22 15:01:59
'''
import os
import hashlib
import time


def print_md5(file_path: str, after: bool, *file_name: str) -> None:
    """打印文件的 md5"""
    with open(file_path, "rb") as f:
        # 获取图片的 md5
        md5 = hashlib.md5(f.read()).hexdigest()
        if after:
          print(' --> {}'.format(md5))
          return ' --> {} \n'.format(md5)
        else:
          print('✅ {}({})'.format(file_name[0], md5), end='')
          return '✅ {}({})'.format(file_name[0], md5)


def change_md5(source_path, log):
    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)

                # 限制只修改 png 文件
                # if ".png" in src_file:

                log.insert('end', print_md5(src_file, False, file))

                # 使用当前时间戳更新 md5
                writefile = int(time.time() * 1000)
                with open(src_file, "a") as f:
                    f.write(str(writefile))

                log.insert('end', print_md5(src_file, True))
        
        print('md5 修改完成!')


