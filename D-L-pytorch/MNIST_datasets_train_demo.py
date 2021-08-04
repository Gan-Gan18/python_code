import torch
from torch import nn
from torch.nn import functional as F
from torch import optim
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision import datasets  # 导入MNIST数据集
from torchvision import transforms  # 数据预处理  数据增强

# 数据预处理  Compose()组合多个预处理操作   ToTensor()将图片转换为Tensor   Normalize([0.5],[0.5])将图片均值标准化
transforms = transforms.Compose([transforms.ToTensor(), transforms.Normalize([0.5], [0.5])])

# 自动下载和加载数据集
train_dataset = datasets.MNIST(root='E:\PycharmProjects\Python\data', train=True, transform=transforms, download=True)
test_dataset = datasets.MNIST(root='E:\PycharmProjects\Python\data', train=False, transform=transforms, download=True)

# 创建数据迭代器  DataLoader()pytorch自带迭代器   batch_size批量送图大小  shuffle=True打乱数据集顺序
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 创建网络
class Net(nn.Module):
    # nn.Sequential()组合网络层  nn.Linear()全连接层/线性层   nn.BatchNorm1d()批标准化
    def __init__(self, in_dim, n_hidden1, n_hidden2, out_dim):
        super(Net, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(in_dim, n_hidden1), nn.BatchNorm1d(n_hidden1))
        self.layer2 = nn.Sequential(nn.Linear(n_hidden1, n_hidden2), nn.BatchNorm1d(n_hidden2))
        self.layer3 = nn.Sequential(nn.Linear(n_hidden2, out_dim))

    # 定义forward正向传播
    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = self.layer3(x)
        return x

# 传入模型参数 各层神经元个数
model = Net(28 * 28, 300, 100, 10)
print(model)

# 定义损失函数和优化器   CrossEntropyLoss()交叉熵损失函数   SDG()随机梯度下降   momentum=0.5动量
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)

# 定义计算资源  'GPU' or 'cpu'
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)  # 将模型放到device上计算

'''
开始训练
'''
# 存储每个epoch的损失值和准确率
train_losses = []
train_accs = []

for epoch in range(20):
    train_loss = 0
    train_acc = 0
    for img, label in train_loader:
        img = img.to(device)  # 将图片放到device上计算
        label = label.to(device)  # 将标签放到device上计算
        img = img.view(img.size(0), -1)  # 将图片变形为model()可接受的参数形式

        # 正向传播
        out = model(img)  # 计算每张图片在各类别上的输出预测值
        loss = criterion(out, label)  # 计算一个batch的损失值

        # 反向传播
        optimizer.zero_grad()  # 梯度归零
        loss.backward()  # 反向传播获得权重的梯度值
        optimizer.step()  # 更新权重

        train_loss += loss.item()  # 将所有batch的损失中累加  item()将标量转换为普通数字
        pred = out.argmax(dim=1)   # 找到batch中各图片预测值的最大值  argmax(dim=1)按列方向找最大值的索引
        train_acc += (pred == label).sum().item() / 64  # 计算一个batch的准确率

    # 计算一个epoch损失值和准确率
    train_loss = train_loss / len(train_loader)
    train_acc = train_acc / len(train_loader)
    train_losses.append(train_loss)
    train_accs.append(train_acc)

    print('Epoch:{}, Train_loss:{:.4f}, Train_acc:{:.4f}'.format(epoch, train_loss, train_acc))
