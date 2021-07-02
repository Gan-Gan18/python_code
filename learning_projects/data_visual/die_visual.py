# 绘制直方图
import pygal
from die import Die

die_1 = Die()
die_2 = Die()
# 设置掷骰子次数以及记录每次掷出的点数
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 统计每个点数出现次数
frequencies = []
max_result = die_1.num_sizes + die_2.num_sizes
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()
hist.title = 'results of rolling two D6 1000 times'
hist.x_labels = list(range(2, max_result+1))
hist.x_title = 'result'
hist.y_title = 'frequency of result'
hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual.svg')
