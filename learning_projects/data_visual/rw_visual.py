import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

# 设置窗口尺寸大小
plt.figure(figsize=(10,6))

# 绘图
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Reds,edgecolors='none',s=15)
plt.scatter(0,0,c='green',edgecolors='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='blue',edgecolors='none',s=100)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()