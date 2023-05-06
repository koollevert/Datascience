import numpy as np
#0-D arrays
arr=np.array(24)
print(arr, "--0-D array")
#1-D arrays
arr1=np.array([1,2,3,4,5])
print(arr1, "--1-D array")
#2-D arrays
arr2=np.array([[1,2,3], [7,4,5]])
print(arr2, "--2-D array")
#3-D arrays
arr3=np.array([[[1,2,3],[4,6,7],[1,9,7]]])
print(arr3,"--3-D array")
#checking type of dimension in an array
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
#arrays can be of any higher dimension
arr4=np.array([1,2,3,4,5,4,5,6,9], ndmin=5) #creating a five dimension array
print(arr4)
print("no of dimensions:", arr4.ndim)

arr5=np.array([[1,2,3],[3,7,6]],ndmin=4)
print(arr5)
print("no of dimensions:", arr5.ndim)