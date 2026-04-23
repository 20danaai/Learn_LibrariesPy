#Lesson 6
import numpy as np
# Arithmetic Operations
my_array=np.array([10,20,30])
my_array1=np.array([5,2,4])
print(my_array+my_array1) # [15 22 34]
print(my_array-my_array1) # [ 5 18 26]
print(my_array*my_array1) # [ 50  40 120]
print(my_array/my_array1) # [ 2.  10.   7.5]
# two Dimiensional Array
my_array2=np.array([[1,4],[5,9]])
my_array3=np.array([[2,7],[10,5]])
print(my_array2+my_array3) # [[ 3 11] [15 14]]
print(my_array2-my_array3) # [[-1 -3] [-5  4]]
print(my_array2*my_array3) # [[ 2 28] [50 45]]
print(my_array2/my_array3) # [[0.5        0.57142857] [0.5        1.8       ]]
# Min,Max,Sum
my_array4=np.array([10,20,30])
print(my_array4.max()) # 30
print(my_array4.min()) # 10
print(my_array4.sum()) # 60
print('*'*30)
my_array5=np.array([[20,300],[200,1000]])
print(my_array5.max()) # 1000
print(my_array5.min()) # 20
print(my_array5.sum()) # 1520
#Ravel
my_array6=np.array([[16,8],[55,4]])
print(my_array6.ravel()) #[16 8 55 4]
my_array7=np.array([[[1,4],[8,0],[5,6],[3,4]]])
print(my_array7.ndim) # 3
print(my_array7.ravel()) # [1 4 8 0 5 6 3 4]
print(my_array7.ndim) # 3
x=my_array7.ravel() 
print(x) # [1 4 8 0 5 6 3 4]
print(x.ndim) # 1
