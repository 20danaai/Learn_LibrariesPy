# Lesson 5
import pandas as pd
olympics=pd.read_excel('ai\data\olympics-data.xlsx')
olympics=olympics.rename(columns={'born_region':'region'}) # without variable or inplace=True  the origonal npt gone change
olympics.head()
bios=pd.read_csv(r'./ai/data/bios.csv')
bios.head()
bios_new=bios.copy()
bios_new['First_name']=bios_new['name'].str.split(' ').str[0]
bios_new
bios_new['born_datetime']=pd.to_datetime(bios_new['born_date'],errors='coerce') # born_date dtype is : str , born_datedime dtype is : datatime
bios_new.info() # There another way use formate "%y_%m_%d" 
bios_new['born_year']=bios_new['born_datetime'].dt.year # Show me just year
bios_new[['name','born_year']]
bios_new.to_csv('./ai/data/bios_new.csv',index=False) # Save all the changes you made in a new external file
bios["height_category"]=bios["height_cm"].apply(lambda x: "short" if x<165 else( 'average' if x<185 else 'tall'))
bios.head()
def categorize_athlete(row):
    if row['height_cm'] < 175 and row['weight_kg']<70:
        return 'light weight'
    elif row['height_cm'] < 185 and row['weight_kg']<80:
        return 'Middle weight'
    else:
        return 'Heavy weight'
bios['category']=bios.apply(categorize_athlete,axis=1) # Means go over the table line by line , axis without it error
