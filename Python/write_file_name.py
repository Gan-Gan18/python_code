import os
file_path=r"E:\dataset\ZhongChe_data\sdg\0319\sdg_images_text_20210319_1_error_result\sdg_images_text_20210319_1"
file_list=os.listdir(file_path)
for file_name in file_list:
    file_list.sort(key=lambda x: str(x.split('.')[0]))
    print(file_name)
    with open(r'E:\dataset\ZhongChe_data\sdg\0319\file_name_1.txt','a')as f:
        f.write(file_name+'\n')
    f.close()