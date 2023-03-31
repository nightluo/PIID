import os
import numpy as np
path='/mnt/data/luoyan/PIID/data/rail'
flist=np.array(os.listdir(path))
train_num=int(0.8*len(flist))
test_num=int(0.9*len(flist))
train_list=flist[0:train_num]
print(train_list)
f=open(r"train.flist","w")
for file in train_list:
    f.write(os.path.join(path,file)+'\n')
f.close()

val_list=flist[train_num:test_num]
f=open(r"val.flist","w")
for file in val_list:
    f.write(os.path.join(path,file)+'\n')
f.close()

test_list=flist[test_num:]
f=open(r"test.flist","w")
for file in test_list:
    f.write(os.path.join(path,file)+'\n')
f.close()
