import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
n = A.shape[0]  #shape可以查看数组的形状
print(A.shape)
#eig_val为特征值,eig_vec为特征向量 且用于方阵
eig_val, eig_vec = np.linalg.eig(A)
print(eig_val)
max_eig_val = np.max(eig_val)
print(max_eig_val)
"""
CI = np.percentile(eig_val, 95)
print(CI)
"""
j = (max_eig_val-3)/2
print(j)
i = [0,0,0,0.52,0.89]
mj = j/i[3]
print(mj)
if mj > 0.1:
    print("不符合一致性检验")
else:
    print("符合一致性检验")
