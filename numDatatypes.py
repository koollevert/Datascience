import numpy as np
arr=np.array(['apple','banana','cherry'])
print(arr.dtype)
#creation of an arrar with datatype string
arr1=np.array([1,2,3,4,5], dtype="S")
print(arr1)
print(arr1.dtype)
#creation of an array of 4 byte interger
arr2=np.array([1,2,3,4,5,6,7],dtype="i4")
print(arr2)
print(arr2.dtype)
#value error
#arr3=np.array(['a','2','3'],dtype="i")
#astype
arr4=np.array([1.2,3.4,5.6,7.1])
newarr=arr4.astype('i')
print(newarr,'--is the new int array')
print(newarr.dtype)
newarr1=arr4.astype('int')
print(newarr1, "--happens when we use int")
print(newarr1.dtype)
newarr2=arr4.astype('bool')
print(newarr2, "--our new bool array")
print(newarr2.dtype)