import pandas as pd
df=pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df.to_string())
#dropna method returns a new dataframe and will not change the original unless inplace true is used
print(df.info)

