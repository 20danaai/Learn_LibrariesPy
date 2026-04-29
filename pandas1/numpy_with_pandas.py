# Lesson 4 
import pandas as pd
bios=pd.read_csv('ai/data/bios.csv')
df_filtered =bios[bios['born_city'].isin(['USA','FRA'])] # Use isin with country,monthhs,(Exact match)(faster)
df_filtered.head()
df_filtered =bios[bios['born_city'].isin(['USA','FRA'])&(bios['name'].str.startswith('Keith'))]
pd_filtered=bios.query('born_country'=='USA'and 'born_city'=='Meulan') # Query is for readable and cleaner code
pd_filtered.head()
# Adding/Removing columns
coffe=pd.read_csv('./Warmup_date/coffe.csv')
coffe['price']=4.99 # That make a new column and the values 4.99
coffe.head()
import numpy as np
new_price1=coffe['new_price']=np.where(coffe['coffe_type']=='Espresso',2.44,5.99) # Use numpy here because she will work like if/else, Condition , True : 2.44, False:5.99
new_price1.head()
coffe.drop(0)
coffe.drop(columns=['price'])
coffe.drop(columns=['price'],inplace=True) # Remove the 'price' column permanently from the datafarm
coffe_new=coffe.copy() # The original schedule is unaffected , Without copy changes will affect the original data
coffe_new['price']=3.6
coffe_new.head()
revenue_column=coffe['revenue']=coffe['units_sold']*coffe['new_price']
revenue_column.head()
