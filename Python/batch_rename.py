import os
import shutil
import datetime

"""
单个文件夹下 对多个文件批量重命名
"""
def backup_files(src_path):
    filenames = os.listdir(src_path)
    for filename in filenames:
        old_name = os.path.join(src_path, filename)
        if os.path.isdir(old_name):
            continue
        shutil.copy(old_name, backup_path)


def batch_rename(src_path, date):
    filenames = os.listdir(src_path)
    same_name = []
    count = 0
    for filename in filenames:
        old_name = os.path.join(src_path, filename)
        if os.path.isdir(old_name):
            continue
        count += 1
        change_name = date + '_%05d' % count + '.' + filename.split('.')[1]
        # change_name = 'single_segmentation_' + date + '_%05d' % count + '.' + filename.split('.')[1]
        new_name = os.path.join(src_path, change_name)
        if change_name in filenames:
            same_name.append(change_name)
            continue
        os.rename(old_name, new_name)
        # result = os.path.basename(old_name) + '->->->->->' + os.path.basename(new_name) + '\n'
        # with open (r'C:\Users\1\Desktop\2\readme.txt','a') as f:
        #     f.write(result)
        # f.close()
    print('\n一共' + str(count) + '个文件,' + '修改了' + str(int(count) - len(same_name)) + '个文件的名字')
    if len(same_name) > 0:
        print('其中有' + str(len(same_name)) + '个文件的原名与新名相同,不作修改')


if __name__ == '__main__':
    date = datetime.datetime.now().strftime('%m%d')
    src_path = r'E:\dataset\ZhongChe_data\sdg\0428_segmentation\single'
    backup_path = src_path + '/' + 'backup/'
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
    backup_files(src_path)
    batch_rename(src_path, date)
