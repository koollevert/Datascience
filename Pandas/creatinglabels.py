import pandas as pd
a=[1,7,2]
myVar=pd.Series(a, index=['x','y','z']) #creating labels
print(myVar) #displaying al of the value by labels
print(myVar['y'])

calories={"day1": 420, "day2":380, "day3":148}
myVar2=pd.Series(calories, index=["day1", "day2"])

print(myVar2)
                
                