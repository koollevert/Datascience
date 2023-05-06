import pandas as pd
data={
    "calories":[420,380,348], "duration":[50,40,45]
}
myVar=pd.DataFrame(data)
print(myVar)
#DataFrames
print("Locate row")
print(myVar.loc[0]) #one location/index
print(myVar.loc[[1,2]]) #two locations/index
print(myVar.loc[[0,1,2]])#notice two sqr bracket for more than one indice
#locations
print("named indexes")
myVar=pd.DataFrame(data,index=["day1", "day2", "day3"])
print(myVar)
#named indexes
print("locate named index")
print(myVar.loc["day2"])
print(myVar.loc[["day1","day3"]])