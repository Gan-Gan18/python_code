import matplotlib.pyplot as plt

#生成散点图
#设置x,y坐标值
x_values = list(range(0,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolors='none',s=40)
plt.title('square numbers',fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('square of value',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])  #设置x和y坐标轴的最小值和最大值
plt.show()
plt.savefig('save.png',bbox_inches='tight')  #保存图表