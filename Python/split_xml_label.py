import os
import os.path
import shutil

fileDir_ann = r'E:\dataset\ZhongChe_data\check_0930\VOC2007\Annotations/'
fileDir_img = r'E:\dataset\ZhongChe_data\check_0930\VOC2007\JPEGImages/'

# 存放包含需要的类的图片
saveDir_img = r'E:\dataset\ZhongChe_data\check_0930\VOC2007\VOC2007_arm\JPEGImages/'

if not os.path.exists(saveDir_img):
    os.mkdir(saveDir_img)

names = locals()

for files in os.walk(fileDir_ann):
    # 遍历Annotations中的所有文件
    for file in files[2]:
        # print
        # file + "-->start!"

        # 存放包含需要的类的图片对应的xml文件
        saveDir_ann = r'E:\dataset\ZhongChe_data\check_0930\VOC2007\VOC2007_arm/Annotations/'

        if not os.path.exists(saveDir_ann):
            os.mkdir(saveDir_ann)
        fp = open(fileDir_ann + file)
        saveDir_ann = saveDir_ann + file
        fp_w = open(saveDir_ann, 'w')
        classes = ['arm', 'luggage', 'pack', 'bag', 'umbrella', 'electronics', 'other']

        lines = fp.readlines()

        # 记录所有的\t<object>\n的位置
        ind_start = []

        # 记录所有的\t</object>\n的位置
        ind_end = []

        lines_id_start = lines[:]
        lines_id_end = lines[:]

        while "\t<object>\n" in lines_id_start:
            a = lines_id_start.index("\t<object>\n")
            ind_start.append(a)
            lines_id_start[a] = "delete"

        while "\t</object>\n" in lines_id_end:
            b = lines_id_end.index("\t</object>\n")
            ind_end.append(b)
            lines_id_end[b] = "delete"

        for k in range(0, len(ind_start)):
            for j in range(0, len(classes)):
                if classes[j] in lines[ind_start[k] + 1]:
                    a = ind_start[k]
                    names['block%d' % k] = lines[a:ind_end[k] + 1]
                    break
        # 需要的类
        classes1 = '\t\t<name>arm</name>\n'
        # classes2 = '\t\t<name>luggage</name>\n'
        # classes3 = '\t\t<name>pack</name>\n'
        # classes4 = '\t\t<name>bag</name>\n'
        # classes5 = '\t\t<name>umbrella</name>\n'
        # classes6 = '\t\t<name>electronics</name>\n'
        # classes7 = '\t\t<name>other</name>\n'
        string_start = lines[0:ind_start[0]]
        string_end = [lines[len(lines)-1]]

        a = 0
        for k in range(0, len(ind_start)):
            if classes1 in names['block%d' % k]:
                a += 1
                string_start += names['block%d' % k]
            # if classes2 in names['block%d' % k]:
            #     a += 1
            #     string_start += names['block%d' % k]
            # if classes3 in names['block%d' % k]:
            #     a += 1
            #     string_start += names['block%d' % k]
            # if classes4 in names['block%d' % k]:
            #     a += 1
            #     string_start += names['block%d' % k]
            # if classes5 in names['block%d' % k]:
            #     a += 1
            #     string_start += names['block%d' % k]
            # if classes6 in names['block%d' % k]:
            #     a += 1
            #     string_start += names['block%d' % k]
            # if classes7 in names['block%d' % k]:
            #     a += 1
            #     string_start += names['block%d' % k]

        string_start += string_end
        for c in range(0, len(string_start)):
            fp_w.write(string_start[c])
        fp_w.close()

        if a == 0:
            os.remove(saveDir_ann)
        else:
            name_img = fileDir_img + os.path.splitext(file)[0] + ".jpg"
            shutil.copy(name_img, saveDir_img)
        fp.close()

