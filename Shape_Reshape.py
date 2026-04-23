# Lesson 7
# NumPy=> Array Shape & Reshape
# Shape Returns Atuple Contains The number Of Elements in Each Dimension
import numpy as np
my_array=np.array([1,3,6,9])
print(my_array.ndim) # 1
print(my_array.shape) # (4,)
my_array1=np.array([[10,30],[20,40],[50,60]])
print(my_array1.ndim) # 2
print(my_array1.shape) # (3,2)
my_array2=np.array([[2,3,4,6],[5,7,99,66]])
print(my_array2.ndim) # 2
print(my_array2.shape) # (2,4)
my_array3=np.array([[[12,34,9],[45,56,8]],[[67,78,7],[89,90,6]]])
print(my_array3.ndim) # 3
print(my_array3.shape) # (2,2,3)
# Reshape
reshaped_array4=my_array3.reshape(3,4)
print(reshaped_array4.ndim) # 2
print(reshaped_array4.shape) # (3,4)
print(reshaped_array4) # [[12 34  9 45] [56  8 67 78] [ 7 89 90  6]]
reshaped_array5=my_array3.reshape(-1) #  Like Ravel
print(reshaped_array5.ndim) # 1
print(reshaped_array5.shape) # (12,)
print(reshaped_array5) # [12 34  9 45 56  8 67 78  7 89 90  6]
my_arrayl=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
reshaped_array6=my_arrayl.reshape(2,5,2)
print(reshaped_array6.ndim) #3 The Num Inside The Brackets Are 3 , Meaning 3
print(reshaped_array6.shape) #(2,5,2)
print(reshaped_array6) # [[[ 1  2] [ 3  4] [ 5  6] [ 7  8] [ 9 10]] [[11 12] [13 14] [15 16] [17 18] [19 20]]]
