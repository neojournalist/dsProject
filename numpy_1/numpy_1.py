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

print()

