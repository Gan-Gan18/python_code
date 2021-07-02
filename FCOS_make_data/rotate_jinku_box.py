import cv2

import numpy as np
import os

def cv_show(name, img):
    """图像显示函数
    name：字符串，窗口名称
    img：numpy.ndarray，图像
    """
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def img_show(name, img):
    """matplotlib图像显示函数
    name：字符串，图像标题
    img：numpy.ndarray，图像
    """
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img, 'gray')
    # plt.xticks([])
    # plt.yticks([])
    plt.xlabel(name, fontproperties='FangSong', fontsize=12)


def rotate_bound(image, angle):
    # 获取图像的尺寸
    # 旋转中心
    (h, w) = image.shape[:2]
    (cx, cy) = (w / 2, h / 2)

    # 设置旋转矩阵
    M = cv2.getRotationMatrix2D((cx, cy), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # 计算图像旋转后的新边界
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # 调整旋转矩阵的移动距离（t_{x}, t_{y}）
    M[0, 2] += (nW / 2) - cx
    M[1, 2] += (nH / 2) - cy

    return cv2.warpAffine(image, M, (nW, nH))


if __name__ == "__main__":
    video_path = r"E:\dataset\jinku_data\box_count\0727\1.mp4"
    if os.path.exists(video_path):
        print("video_path exits")
    cap = cv2.VideoCapture(video_path)
    save_path = "E:\\dataset\\jinku_data\\box_count\\0727\\img\\"+os.path.basename(video_path).split(".mp4")[0]
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    count=0
    c=0
    while (1):
        ret, frame = cap.read()
        frame = cv2.resize(frame,(1280,720))
        cv2.imwrite("./720.jpg",frame)
        # get a frame
        count += 1

        if count % 50 == 0:
            img1 = frame.copy()
            angle = 25
            name = save_path +"\\count_0727_"+os.path.basename(video_path).split(".mp4")[0]+"%06d" % (count)+"_"+str(angle) + ".jpg"
            img2 = rotate_bound(img1,angle)
            cv2.imwrite(name,img2)
            c+=1
            print(c)




























































