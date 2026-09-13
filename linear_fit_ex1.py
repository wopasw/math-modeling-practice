import numpy as np
# 习题1：最小二乘线性拟合
x = np.array([1,2,3,4,5])
y = np.array([2.1,2.9,4.2,4.9,6.0])
a,b = np.polyfit(x,y,1)
print(f"a = {a:.2f}, b = {b:.2f}")
y_pred = a*6 + b
print(f"x=6时预测y={y_pred:.2f}")
