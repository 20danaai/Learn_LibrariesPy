#lesson 4
#slicing[Start,End,Steps]
import numpy as np
a=np.array(['a','b','c','d','e','f'])
print(a.ndim)#1
print(a[1])#b
print(a[1:4])#['b' 'c' 'd']
print(a[:4])#['a' 'b' 'c' 'd']
print(a[2:])#['c' 'd' 'e' 'f']
print('*'*50)
b=np.array([['a','b','x'],['c','d','y'],['e','f','z'],['m','n','o']])
print(b.ndim)#2
print(b[1])#['c' 'd' 'y']
print(b[:3])#[['a' 'b' 'x']
 #['c' 'd' 'y']
 #['e' 'f' 'z']]
print(b[:3,:2])#[['a' 'b']
 #['c' 'd']
 #['e' 'f']]
print(b[2:,:2])#[['e' 'f'] ['m' 'n']]
print(b[:2, :2:2])#[['a']
 #['c']]
