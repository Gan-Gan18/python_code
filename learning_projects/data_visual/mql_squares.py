import matplotlib.pyplot as plt

#生成折线图
input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.plot(input_value,squares,linewidth=5)  #plot() 绘制图形，设置线条粗细
plt.title('square numbers',fontsize=24)  #设置标题
plt.xlabel('value',fontsize=14)  #设置坐标标签
plt.ylabel('square of value',fontsize=14)
plt.tick_params(axis='both',labelsize=14)  #设置刻度

plt.show()  #显示图形
