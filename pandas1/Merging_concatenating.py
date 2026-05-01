
import pandas as pd
bios=pd.read_csv('./ai/data/bios.csv')
nocs=pd.read_csv('ai/data/noc_regions.csv')
nocs.head()
bios_new=pd.merge(bios,nocs,left_on='born_country',right_on='NOC',how='left')
# We have 4 basic types : Everything on the left + the matching item on the right(the rest is empty)
# how='right': Reverse left , how='inner': Only the rows that have a 100% match on both sides , how='outer' : All rows from both ends , with the spaces filled with NaN
bios_new.head()
#bios_new=pd.merge(bios,nocs,left_on='born_country',right_on='NOC',how='left',suffixes=['bios','nocdf']) # Suffix for rename NOC_x from first file + NOC_y from seconde file
bios_new.rename(columns={'region' : 'born_country_full'},inplace=True)
bios_new
bios_new[bios_new['NOC_x']!=bios_new['born_country_full']][['name','NOC_x','born_country_full']] # To detect errors in the data
usa=bios[bios['born_country']=='USA'].copy()
gbr=bios[bios['born_country']=='GBA'].copy()
usa.head()
gbr.head()
new_df=pd.concat([usa,gbr])# usa : top , gbr : bottom
new_df
