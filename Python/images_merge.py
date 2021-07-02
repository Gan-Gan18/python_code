import shutil,os
new_path=r'F:\test_20210318\images_merge_20210319_1'
for derName, subfolders, filenames in os.walk(r'F:\test_20210318\sdg_detect_videos'):
    print(derName)
    print(subfolders)
    print(filenames)
    for i in range(len(filenames)):
        if filenames[i].endswith('.jpg'):
            file_path=derName+'/'+filenames[i]
            newpath=new_path+'/'+filenames[i]
            shutil.copy(file_path,newpath)
