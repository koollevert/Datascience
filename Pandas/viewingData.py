import pandas as pd
df=pd.read_csv('data.csv')
print(df.head(10))#printing first ten rows, if head no not specified then first five row are then printed instead
print(df.head())
#tail()method
print(" tail() Method")
print(df.tail(10))#last ten rows printed
 #info() method of DataFrames object
print("#info() ")
print(df.info())
 
