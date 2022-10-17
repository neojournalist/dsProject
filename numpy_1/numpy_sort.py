import numpy as np

array1_1d = np.random.randint(10,70, size =(7))
print(array1_1d)

array1_2d = np.random.randint(10,70, size =(4,4))
print(array1_2d)

#Sorting
array1_1d = np.sort(array1_1d)
print(array1_1d)

array1_2d = np.sort(array1_2d)
print(array1_2d)

np.sort(array1_2d, 0) #sorting by columns (axis - 0)
print(array1_2d)

np.sort(array1_2d, 1) # sorting by rows (axis - 1)
print(array1_2d)

#sort using data type
dt = np.dtype([('fullname', 'S10'),('age', int)])
print(dt)

workerArrays = np.array([('Asan Gaparov', 30),('Bermet Akerova', 25), ('Elena Prokofyeva', 32), ('Timur Bogdanov', 43)], dtype=dt)
print(workerArrays)

np.sort(workerArrays, order = 'fullname')

#sorying woth argsort() by indexes
a1 = np.array([7,2,4,5])
a2 = np.argsort(a1)
print(a1[a2])

for i in a2:
    print(a1[i], end=" ")

#Function lexsort() sort by keys
workersKey = ('Bermet', 'Yulia', 'Oleg', 'Asan', 'Murat')
idWorkers = ('b.t.', 'y.l.', 'o.g', 'a.t.', 'm.k')
worker = np.lexsort((workersKey, idWorkers))
print(worker)
listofWorkers = [workersKey[i] + ", "+idWorkers[i] for i in worker]
# for i in worker:
# listofWorkers = workersKey[i] + ", " + idWrokers[i]
print(listofWorkers)

#max and min element of an array argmax(), argmin()
print(np.argmax(array1_1d))
print(np.argmax(array1_2d, 0))
print(np.argmin(array1_1d))
print(np.argmin(array1_2d, 1))

#flatten
min_index = np.argmin(array1_1d)
print(array1_1d.flatten()[min_index])
max_index = np.argmax(array1_1d)
max_2d_index = np.argmax(array1_2d)
print(array1_1d.flatten()[max_index])
print(array1_2d.flatten('K')[max_2d_index])
max_2d_index_axis0 = np.argmax(array1_2d, 0)
print(array1_2d.flatten('C')[max_2d_index_axis0])

array3d = np.array(
   [ [12,0,34],
    [34,5,0],
    [0,11,0]]
)
np.nonzero(array3d)

for i in [123,4,5]:
    if i == 4:
        continue
    print(i)

larger41 = np.where(array1_2d > 41)
print(larger41)
larger34 = np.where(array1_1d > 34)
print(larger34)
smaller41 = np.where(array1_2d < 41)
print(smaller41)

#Condition - Extract()
conditionExtract = np.mod(array1_2d, 2) == 0
evenNumb = np.extract(conditionExtract, array1_2d)
print(evenNumb)

conditionExtract2 = np.mod(array1_2d, 2) == 1
oddNumb = np.extract(conditionExtract2, array1_2d)
print(oddNumb)


