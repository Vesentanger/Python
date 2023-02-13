# 输入摄氏度转为华氏度
import math

rad = float(input('半径：'))
height = float(input('高：'))

area = rad * rad * math.pi
print('面积是：' + str(area))
volume = area * height
print('体积是：' + str(volume))
