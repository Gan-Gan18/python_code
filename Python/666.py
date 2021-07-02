import os
import shutil
import datetime

def batch_rename(src_path, date):
    filenames = os.listdir(src_path)
    same_name = []
    count = 0
    for root, dirs, files in os.walk(src_path):
        for filename in files:
            old_name = os.path.join(root, filename)
            count += 1
            change_name = date + '_%05d' % count + '.' + filename.split('.')[1]
            new_name = os.path.join(root, change_name)
            if change_name in filenames:
                same_name.append(change_name)
                continue
            os.rename(old_name, new_name)
    print('\n一共' + str(count) + '个文件,' + '修改了' + str(int(count) - len(same_name)) + '个文件的名字')
    if len(same_name) > 0:
        print('其中有' + str(len(same_name)) + '个文件的原名与新名相同,不作修改')


if __name__ == '__main__':
    date = datetime.datetime.now().strftime('%m%d')
    src_path = r'C:\Users\1\Desktop\1\2'
    batch_rename(src_path, date)