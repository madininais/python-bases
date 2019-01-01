import numpy as np

np.array([1,2,3,4,5], dtype = 'float32')
np.zeros(10, dtype = int)
np.ones((3,5), dtype = float)
np.full((3,5), 3.14)
np.eye(3) # 3x3 identity matrix

np.arange(0,20,5) #linear sequence starting from 0 ending at 20 stepping by 5
np.linspace(0,1,5) #5 values evenly saced between 0 and 1

np.random.random((3,3)) # 3x3 array random values between 0 and 1
np.random.normal(0,1,(3,3)) # 3x3 array of normally distributed random values with mean 0 and sd 1
np.random.randint(0,, 10, (3, 3)) # 3x3 array of ranom integers in 0,10

np.random.seed(0)  # seed for reproducibility

x[::2]  # every other element
x[1::2]  # every other element, starting at index 1
x[::-1]  # all elements, reversed
print(x2[0])  # equivalent to x2[0, :]

x2_sub_copy = x2[:2, :2].copy() #If we now modify this subarray, the original array is not touched

np.arange(1, 10).reshape((3, 3))

x[np.newaxis, :] # row vector via newaxis
x[:, np.newaxis] # column vector via newaxis


np.concatenate([grid, grid]) # concatenate along the first axis
np.concatenate([grid, grid], axis=1) # concatenate along the second axis (zero-indexed)
np.vstack([x, grid]) # vertically stack the arrays
np.hstack([grid, y]) # horizontally stack the arrays

x1, x2, x3 = np.split(x, [3, 5]) 
upper, lower = np.vsplit(grid, [2])
left, right = np.hsplit(grid, [2])

np.sum(x < 6, axis=1)
np.any(x < 0)
np.all(x < 10)


M.shape
M.reshape((3,1))


## sorting arrays
np.sort(x)
np.sort(x, axis=0) #sort each column of x
np.partition(x, 3) #the smallest k values to the left + raminings


## strcutured array
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
							'formats':('U10', 'i4', 'f8')})
data['names']=[bla,bla,bla]
data['age']=[bla,bla,bla]
data['weight']=[bla,bla,bla]


## NumPy’s datetime64
date = np.array('2015-07-04', dtype=np.datetime64)
date + np.arange(12)
np.datetime64('2015-07-04 12:00')



