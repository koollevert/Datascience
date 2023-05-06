import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,])
print(arr[-3]) #accessing third last element in the array
#addding element by index number
print(arr[0]+arr[1], "--is the sum of the 1st & 2nd figure in the arr")
#accessing elements of 2-D array
arr1=np.array([[1,2,3,9,6,3,5], [4,5,6,1,7,9,6]])
print(arr1[0,1],"--2nd element on the first row")#row, element in that order
print(arr1[1,4],"--5th element on the second row")
print(arr1[0,1]+arr1[1,4], "--is the sum")
arr3=np.array([[[8,5,6,5,6,8,9], [4,5,3,6,7,1,4]], [[5,8,9,5,6,4,3],[2,5,6,7,4,5,9]]])
print(arr3.ndim, "--is the dimension the array")
print(arr3)
print(arr3[0,1,4],"--dim, array, element position")#just like the brackets goes dimension, array element in that order