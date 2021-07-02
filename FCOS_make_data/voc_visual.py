import cv2
import os
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
root_xml = r"E:\dataset\jcp_data\hat_clothes\VOC2007_0518\Annotations/"
rootDir = r"E:\dataset\jcp_data\hat_clothes\VOC2007_0518\JPEGImages/"
save_folder=r"E:\dataset\jcp_data\hat_clothes\VOC2007_0518/result/"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
error = []
# label_name = {"5":(255,255,255),"2":(255,0,0),"1":(0,0,255),"3":(0,255,255),"4":(0,255,0),'6':(255,23,89)}
# label_name = {"0":(0,0,0),"1":(255,255,255),"2":(255,0,0),"3":(0,0,255),"4":(0,255,255),"5":(0,255,0)}
# label_name = {"1":(255,255,255),"2":(255,0,0),"3":(0,0,255),"0":(0,255,255)}
# label_name = {"11":(0,255,255),"13":(0,0,255),"18":(0,0,0),"22":(255,0,0)}
# label_name = {"4":(255,255,255),"5":(255,0,0)}
# label_name = {"6":(0,0,0),"7":(0,0,255),"8":(0,255,255),"9":(255,255,255),"10":(255,255,0),"11":(255,0,0),"12":(0,255,0),
#               "13":(255,0,255),"14":(255,23,89),"15":(0,100,98),"16":(100,0,98),"17":(255,89,23),"18":(0,98,100)}
# label_name = {"none":(0,0,0),"red":(0,0,255),"other":(0,100,98),"blue":(255,0,0),"white":(255,255,255),"black":(0,0,0),"green":(0,255,0)}
# label_name={"front":(0,255,0),"back":(255,0,0)}
# label_name = {"1":(0,0,255),"2":(0,255,0)}
#检测棚
# label_name = {"light":(0,255,0),"flicker":(255,0,0),"dark":(0,0,255)}
# label_name = {"pole":(0,255,0)}
# label_name = {"1":(0,255,0)}
# label_name = {"open":(0,255,0),"close":(255,0,0)}
# label_name = {"clothes":(0,0,255),"rope":(255,0,0)}
label_name = {"head0":(0,0,0),"head1":(255,0,0),"head2":(0,255,255),"clothes0":(0,0,0),"clothes1":(255,0,0),"clothes2":(0,255,255)}
#moneybag
# label_name = {"1":(255,255,255),"2":(255,0,0),"3":(0,0,255),"4":(0,255,255)}
# label_name = {"moneybag":(255,255,255),"box":(255,0,0)}
# label_name = {"luggage":(0,0,0),"pack":(0,0,255),"head2":(0,100,98),"clothes0":(255,0,0),"clothes1":(255,255,255),"clothes2":(0,0,0)}
# label_name = {"arm":(0,255,0)}
def parse_xml(xml_file):
    tree = ET.parse(root_xml + xml_file)  # <class 'xml.etree.ElementTree.ElementTree'>
    root = tree.getroot()
    bboxes = []
    color =[]
    for obj in root.findall('object'):
      bbox = obj.find('bndbox')
      label = obj.find('name').text
      #print(label)
      # if label!="clothes":
      #     error.append(root_xml + xml_file)
      #     print(label)
      #     print(root_xml + xml_file)
          # print("mmm")
      bboxes.append((int(bbox.find('xmin').text),
                     int(bbox.find('ymin').text),
                     int(bbox.find('xmax').text),
                     int(bbox.find('ymax').text),
                     label))

    return bboxes

def listDir(rootDir, image_list,endwith):
    files = os.listdir(rootDir)
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if os.path.isfile(pathname):
            if pathname.split(".")[-1] in [endwith]:
                image_list.append(pathname)
        else:
            listDir(pathname, image_list,endwith)


image_list = []
listDir(rootDir, image_list,"jpg")



for i in range(len(image_list)):
    name_index = int(os.path.basename(image_list[i]).split(".jpg")[0])


    img = cv2.imread(image_list[i])
    xml_name = os.path.basename(image_list[i]).split(".jpg")[0]+".xml"

    #print(xml_name)
    xml_names=root_xml + xml_name
    if os.path.exists(xml_names) is False:
        continue
    bboxes= parse_xml(xml_name)
    # for x in error:
    #     if (os.path.exists(x)):
    #         os.remove(x)
    #         print(x)
    #         os.remove(image_list[i][0])

    for box in bboxes:
        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), label_name[box[4]], 2)

        name=save_folder+os.path.basename(image_list[i])
        cv2.putText(img, box[4], (box[2], box[3]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        cv2.imwrite(name,img)

# cv2.imshow("", img)
# cv2.waitKey()
        print(i)



