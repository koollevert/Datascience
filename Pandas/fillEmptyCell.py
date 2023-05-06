import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())

df.fillna(130, inplace=True)
print(df.to_string())