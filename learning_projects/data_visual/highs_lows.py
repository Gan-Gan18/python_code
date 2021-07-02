import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 打开文件
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 遍历文件内的日期和气温值，存储在列表中
    dates,highs,lows = [],[],[]  #创建存储日期和最高气温的列表
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')  #strptime()转换日期格式
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# 绘制图表
fig = plt.figure(figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)  #实参alpha设置颜色透明度
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)  #fill_between()填充区域颜色
plt.title('daily high and low temperatures-2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()  #绘制倾斜的日期标签
plt.ylabel('temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()