import pandas as pd
df=pd.read_csv('data.csv')
x=df["Calories"].mean() #can use here mode() median() also
df["Calories"].fillna(x, inplace=True)
print(df.to_string())
