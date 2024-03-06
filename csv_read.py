#csv read 
import pandas as pd

df = pd.read_csv('pokemon.csv')

print(df['Name'])

#for loop
for r, rij in df.iterrows():
    print(rij["Name"])