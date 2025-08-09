# Ax = B
import numpy as np
A = np.array([1,2,3,4])
B = np.array([[5,6], [7,8], [9,10]])

A1 = A.reshape(2, 2)
B1 = B.T

x = np.matmul(np.linalg.inv(A1),B1)

print(f"x: {x}")