import numpy as np


myList = [213, True, 'S']
arrayn1 = [23, 45, 5]
arrays = ['s', 't', 'hello']

# NumPy = Numerical Python
# array in numpy = ndarray

#creating array
arr = np.array([1, 2, 32, 43, 5])
print(type(arr))
print(np.__version__)

arr2d = np.array(
    [
        [1, 2, 32, 43, 5],
        [2, 4,5,6,5]
    ]
)
print(arr2d)

arr3d = np.array(
    [[
        [1, 2, 32],
        [2, 4, 5],
        [6, 7, 2]
    ],
    [
        [1, 2, 32],
        [2, 4, 5],
        [6, 7, 2]
    ]]
)
print(arr3d)
print(arr3d[1][1][1])
print(arr.ndim)
print(arr2d.ndim)

arr4d = np.array([2,3,5], ndmin =4)
print(arr4d)

print(arr2d)
arr2d.sort()
print(arr2d)

print(arr3d)
arr3d.sort()

print(arr3d[0][-1][-2])
myListNumb = [34, 5, 6, 7, 8]
print(myListNumb[1:3])
print(myListNumb[-4:])

arr1d_two = np.array([34, 5, 2, 5, 4])
arr2d_two = np.array([
    [23, 45, 6, 87],
    [34, 5, 6, 23],
    [56, 8, 9, 10],
    [15, 93, 41, 6]
])

print(arr1d_two[2:])
print(arr2d_two[2, 1:3]) #print(arr2d_two[2][1:3])

#Data type in Numpy
"""
i = Integer
b = Boolean
u = unsigned integer (1, 2, 3, ...)
f = float (23.34, 45.7)
cf = complex float (0.23412)
M = datetime
O = objects
S = string
U = symbols
V = fixed number of memory
"""

print(arr2d_two.dtype)
s = np.array(['s', 'hello', 'tr'])
print(s.dtype)

fnumbers = np.array([23.45, 34.1, 45.11])
print(fnumbers.dtype)

copy2dArr = arr2d_two.copy()
print(arr2d_two)
print('===')
print(copy2dArr)
copy2dArr[1][0] = 11
print(arr2d_two)
print('===')
print(copy2dArr)
print('*' * 50)

view_2darray = arr2d_two.view()
print(arr2d_two)
print('======')
print(view_2darray)
view_2darray[2][1] = 13
print(arr2d_two)
print('======')
print(view_2darray)

# to check the array shape
print(arr2d_two.shape)
print(arr3d.shape)

# reshaping an array
singleArray1d = np.array([3,24,43,23,12,65,7,2,19,10,45,29])
print(singleArray1d)
newArr = singleArray1d.reshape(2,3,2)
print(newArr)

#arrays iteration
print(singleArray1d)
for i in singleArray1d:
    print(i, end=" ")

print(copy2dArr)
for row in copy2dArr:
    for el in row:
        print(el, end=' ')

print(arr3d)
print("=======")
for twod in arr3d:
    for row in twod:
        for el in row:
            print(el, end=" ")
        print()
    print()