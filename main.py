import pandas as pd
import csv 

df=pd.read_csv("final.csv")

print(df.shape)

del df["Luminosity"]
del df["Star_name2"]
del df["Distance2"]
del df["Mass2"]
del df["Radius2"]

print(df.shape)
df=df.rename({
    'st_hostname':'Star_name1',
    'st_dist':'Distance1',
    'st_mass':'Mass1',
    'st_rad':'Radius1'

})

df.to_csv("main.csv")