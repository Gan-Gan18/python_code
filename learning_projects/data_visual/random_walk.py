from random import choice

#生成随机漫步数据的图表
class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points = num_points
        #从坐标(0,0)开始
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:  #用循环实现随机漫步
            #随机选取方向和距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            # 随机选取一个整数作为y坐标值
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #不在原地
            if x_step == 0 and y_step == 0:
                continue
            #计算下一次移动的坐标值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            #将下一次坐标值添加到列表
            self.x_values.append(next_x)
            self.y_values.append(next_y)
