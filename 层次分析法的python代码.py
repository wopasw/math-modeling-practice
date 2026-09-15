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
