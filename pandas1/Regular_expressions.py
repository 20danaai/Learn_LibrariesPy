# Lesson 3
# r : Raw string , ^ : Start from the begining of the line , $ : End , . : Means any letters , \1: Search the smae letters that you save in te group 1
# [^]: Not in , *: Frequency , + : At least one don'nt accept zero freq
# na = False : if you see None follow your work
import pandas as pd
bios=pd.read_csv('ai/data/bios.csv')
# 1) Find athletes born in cities that start with a vowel:
vowel_cities=bios[bios['born_city'].str.contains(r'^[AEIOUaeiou]',na=False)]
# 2) Find athletes with names that contain exactly two vowels:
two_vowel=bios[bios['name'].str.contains(r'^[^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*$',na=False)]
# 3) Find athletes with names that have repeated consecutive letters(e.g.,'Aaron','Emmett'):
repeated_letters=bios[bios['name'].str.contains(r'(.)\1',na=False)]
# 4) Find athletes with names ending in 'son' or 'sen':
son_sen_names=bios[bios['name'].str.contains(r'son$|sen$',case=False,na=False)]
# 5) Find athletes born in a year starting with '19':
born_19xx=bios[bios['born_date'].str.contains(r'^19',na=False)]
# 6) Find athletes with names that do not contain any vowels:
no-vowels=bios[bios['name'].str.contains(r'^[^AEIOUaeiou]*$',na=False)]
# 7) Find athletes with names contains a hyphen or an apostrophe:
hyphen_apostrophe=bios[bios['name'].str.contains(r"[_']",na=False)]
# 8) Find athletes with names that start and end with the same letter:
start_end_same=bios[bios[bios['name'].str.contains(r"[^(.).*\1$]",na=False)]] # . : Means middle
# 9) Find athletes with a born_city that has exactly 7 characters:
city_seven_chars=bios[bios['born_city'].str.contains(r'^.{7}$',na=False)]
# 10) Find athletes with names containing three or more vowels:
three_or_more_vowels=bios[bios['name'].str.contains(r"([AEIOUaeiou].*){3,}",na=False)]
