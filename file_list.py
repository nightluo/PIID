import os


def write_line(writing_file, content):
    writing_file.write(content + "\n")


path = '../data/rail_normal'
output_path = './data/rail_normal'
dir_list = os.listdir(path)
# num_files = len(dir_list)
num_files = int(len(dir_list) / 2) # 硬写，特殊处理的
train_rate = 0.7
val_rate = 0.1
train_list_file = open(os.path.join(output_path, "train.flist"), 'w')
test_list_file = open(os.path.join(output_path, "test.flist"), 'w')
val_list_file = open(os.path.join(output_path, "val.flist"), 'w')

num_write = 0
# writing_file = train_list_file

for file in os.listdir(path):
    if file.endswith(".png"):
        if num_write > int(num_files * (train_rate + val_rate)):
            # print('test',num_write)
            write_line(test_list_file, str(os.path.join(path, file)))
        elif num_write > int(num_files * train_rate):
            # print('val',num_write)
            write_line(val_list_file, str(os.path.join(path, file)))
        else:
            write_line(train_list_file, str(os.path.join(path, file)))

        num_write += 1

train_list_file.close()
test_list_file.close()
val_list_file.close()

print(num_write)
