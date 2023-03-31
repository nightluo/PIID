'''
Author: nightluo 1872194982@qq.com
Date: 2023-03-31 10:21:00
LastEditors: nightluo 1872194982@qq.com
LastEditTime: 2023-03-31 13:59:35
FilePath: /road/PIID/file_list_dir.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os


def write_line(writing_file, content):
    writing_file.write(content + "\n")


path = './dataset/train'
output_path = './dataset/flist'
dir_list = os.listdir(path)
num_files = len(dir_list)
train_list_file = open(os.path.join(output_path, "train.flist"), 'w')

writing_file = train_list_file

for file in os.listdir(path):
    if file.endswith(".JPG") or file.endswith(".jpg"):
        new_name = file.replace('JPG', 'jpg')
        old = os.path.join(path, file)
        new = os.path.join(path, new_name)
        os.rename(old, new)
        write_line(train_list_file, str(new))


train_list_file.close()
