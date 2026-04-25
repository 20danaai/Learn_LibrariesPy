import pandas as pd
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]]) 
#   0  1  2
#0  1  2  3
#1  4  5  6
#2  7  8  9
print(df.head())
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["A",'B','C'])
print(df.head())
#   A  B  C
#0  1  2  3
#1  4  5  6
#2  7  8  9
print(df.head(1))
#   A  B  C
#0  1  2  3
print(df.tail(1))
#   A  B  C
#2  7  8  9
print(df.columns) #Index(['A', 'B', 'C'], dtype='str')
print(df.index)#RangeIndex(start=0, stop=3, step=1)
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["A",'B','C'],index=["X","Y","Z"])
print(df.index)#Index(['X', 'Y', 'Z'], dtype='str')
print(df.info())
print(df.describe())
print(df.nunique())#Count unique values in each column 
print(df["A"].nunique())# Just for A column
print(df.shape)#(3, 3)
