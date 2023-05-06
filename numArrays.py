import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr)) #type:py function telling type of object passed to it
#lists tupples can be passed into array() and will be converted to ndarray
arr2=np.array((1,2,3,4,5))
print(arr2)
arr3=np.array({1,2,3,4,5})
print(arr3) #but a dictionarry is different
print(arr3.dtype)