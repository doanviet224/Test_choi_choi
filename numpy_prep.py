import numpy as np
'''
arr = np.array([5, 4, 3, 2, 1])
print(arr)

#np.sort(arr) # This sorts the array in place, but does not return a new array
print(np.sort(arr)) # Sorts the array in ascending order
print(np.sort(arr)[::-1]) # Sorts the array in descending order


print(np.empty(4)) # Creates an array of uninitialized values
print(np.zeros(2)) # Creates an array of zeros
print(np.ones(4)) # Creates an array of ones
#np.arange
print(np.arange(5)) # Creates an array with values from 0 to 4
print(np.arange(2, 10)) # Creates an array with values from 2 to 9
print(np.arange(2, 9, 2)) #Step of 2

#np.linspace
print(np.linspace(0, 10, num=5)) # Creates an array with 5 values evenly spaced between 0 and 10
print(np.linspace(0, 10, num=5, endpoint=False)) # Excludes the endpoint, creating 5 values between 0 and 10
print(np.linspace(0, 10, num=5, retstep=True)) # Returns the step size along with the array

#np.concatenate Nối hai mảng lại với nhau
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a, b)))

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
print(np.flip(a)) # lật ngược
print(np.unique(a)) # bỏ trùng (giống set(array))


arr1 = np.array([1.1, 2.1, 3.1])
newarr = arr1.astype('i')
print(newarr)
print(newarr.dtype)

#ndim: Ép số chiều của mảng
arr2 = np.array([1, 2, 3, 4], ndmin=5)
print(arr2)
print('shape of array :', arr2.shape)

#reshape: Thay đổi kích thước của mảng
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr3 = arr3.reshape(4, 3)
print(newarr3)

#flaten: Chuyển đổi mảng đa chiều thành mảng một chiều
# -1: Tự động tính toán kích thước của mảng một chiều
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
newarr4 = arr4.reshape(-1)
print(newarr4)

#eye: Tạo ma trận đơn vị (identity matrix)
arr5 = np.eye(3)
print(arr5)

#transpose: Chuyển vị ma trận
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.transpose(A))

#np.linalg.det: Tính định thức của ma trận
B = np.array([[2, 1, 3], [5, 3, 2], [1, 4, 3]])
print(np.linalg.det(B))  # Tính định thức của ma trận B

#np.linalg.inv: Tính ma trận nghịch đảo
C = np.array([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
print(np.linalg.inv(C))

#np.matmul: Nhân ma trận
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[7, 8],
              [9, 10],
              [11, 12]])
print(np.matmul(a,b))
'''