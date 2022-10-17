import numpy as np

arr1d = np.random.randint(30,100, size =(6))
arr3d = np.random.randint(20,90, size=(3,3,4))
print(arr3d)

min_index = np.argmin(arr3d)
max_index = np.argmax(arr3d)
print(arr3d.flatten()[max_index])
print(arr3d.flatten()[min_index])

dp = np.dtype([('fullname', 'S10'),('title', 'S10'),('salary', int)])
print(dp)

arrayDB =([('Pam Mix', 'director', 2000), ('Ben Shirley', 'accountant', 1000), ('Steve Jobs', 'manager', 800), ('Colin Firth', 'salesperson', 900)], dp)
print(arrayDB)

# np.sort(arrayDB, order='fullname')
# np.sort(arrayDB, order='title')
# np.sort(arrayDB, order='salary')

arr2d = np.random.randint(50,150, size=(4,4))
print(arr2d)

larger100 = np.where(arr2d > 100)
print(larger100)