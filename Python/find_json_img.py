#  标注图像后JSON文件与JPG图像在一个文件夹内
#  而我们只需要标注的图像和对应的JSON文件
#  本程序功能把存放在素材文件夹中的标注图像和对应JSON文件分别保存至指定文件夹
#  LB
import sys
import os, random, shutil


def extract_name(Image_dir, write_file_name):
    file_list = []
    #  读取文件，并将地址、图片名和标签写到txt文件中
    write_file = open(write_file_name, "w")  # 打开write_file_name文件
    for file in os.listdir(Image_dir):
        if file.endswith(".json"):
            name = file.split('.')[0]  # JSON名称和后缀名
            write_name = name
            file_list.append(write_name)
    sorted(file_list)  # 将列表中所有元素随机排列
    number_of_lines = len(file_list)
    for current_line in range(number_of_lines):
        write_file.write(file_list[current_line] + '\n')
    write_file.close()


def moveJPG(fileLabelDir, write_file_name):
    pathDir = os.listdir(fileLabelDir)
    f = open(write_file_name, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')  # 去除文本的换行符，否则报错
        shutil.move(fileLabelDir + str(line) + '.jpg', tarJPGDir + str(line) + '.jpg')


def moveJSON(fileLabelDir, write_file_name):
    pathDir = os.listdir(fileLabelDir)
    f = open(write_file_name, 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')  # 去除文本的换行符，否则报错
        shutil.move(fileLabelDir + str(line) + '.json', tarJSONDir + str(line) + '.json')


if __name__ == '__main__':
    Image_dir = r'C:\Users\1\Desktop\output/'  # 原JPG与JSON存放文件夹
    write_file_name =r'C:\Users\1\Desktop\output\dir.txt'  # 提取JSON文件名保存地址
    fileLabelDir = Image_dir
    tarJPGDir = r'C:\Users\1\Desktop\jpg/'    # JPG存放地址
    if not os.path.exists(tarJPGDir):
        os.makedirs(tarJPGDir)
    tarJSONDir = r'C:\Users\1\Desktop\json/'  # JSON存放地址
    if not os.path.exists(tarJSONDir):
        os.makedirs(tarJSONDir)
    extract_name(Image_dir, write_file_name)
    moveJPG(fileLabelDir, write_file_name)
    moveJSON(fileLabelDir, write_file_name)
