#lesson2
#compare performance and memory use
import numpy as np
import time
import sys
elements=150
my_list=range(elements)
my_list2=range(elements)
for i in my_list:
    print(i)
my_array=np.arange(elements)
my_array2=np.arange(elements)
for i in my_array:
    print(i)
list_start=time.time()
for n1,n2 in zip(my_list,my_list2):
    print(n1+n2)
list_result=[(n1+n2) for n1,n2 in zip(my_list,my_list2)]
array_start=time.time()
array_result=my_array+my_array2# array don't need for loop 
print(array_result)
print('*'*30)
print(f'List time :{time.time()-list_start}')#List time :0.03212404251098633
print(f'Array time {time.time()-array_start}')#Array time 0.002579212188720703
print('*'*30)
#
array=np.arange(100)
print(array.itemsize)#How many bites does it take
print(array.size)#Number of items inside 
print(f'All Bites:{array.itemsize*array.size}')#All Bites:800,less
#Bites List
list_size=range(100)
print(sys.getsizeof(1))
print(sys.getsizeof(list_size[0]))#Another way
print(sys.getsizeof(list_size[1]))
print(len(list_size))
print(f'All Bites{sys.getsizeof(1)*len(list_size)}')#All Bites2800,more
