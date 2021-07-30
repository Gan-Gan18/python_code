# import os
# import random
# import shutil
#
# ori_dir = r'Y:\Data\ZNJT\ZhoneChe_sdg_blur_check\LabelData\20210722\clear'
# copy_dir = r'Y:\Data\ZNJT\ZhoneChe_sdg_blur_check\LabelData\20210722\clear_01'
# files = os.listdir(ori_dir)
# file_list = []
# for file in files:
#     file_list.append(file.split('.')[0])
#
# sample = random.sample(file_list, 3000)
# # print(len(sample))
# for name in sample:
#     print(name)
#     shutil.move(ori_dir + '/' + name + '.jpg', copy_dir)
#     # shutil.copy(ori_dir + '/' + name + '.json', copy_dir)


from torch import nn
from torch.nn import functional as F


class Net(nn.Module):

    def __init__(self, in_dim, n_hidden1, n_hidden2, out_dim):
        super(Net, self).__init__()

        self.layer1 = nn.Sequential(nn.Linear(in_dim, n_hidden1), nn.BatchNorm1d(n_hidden1))
        self.layer2 = nn.Sequential(nn.Linear(n_hidden1, n_hidden2), nn.BatchNorm1d(n_hidden2))
        self.layer3 = nn.Sequential(nn.Linear(n_hidden2, out_dim))

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = self.layer3(x)
        return x


model = Net(28 * 28, 300, 100, 10)
print(model)