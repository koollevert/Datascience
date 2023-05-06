import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())
print(" ")
print(" ")
print("print max no of rows")

print(pd.options.display.max_rows)