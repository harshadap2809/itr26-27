import numpy as np

# Array Creation
# Creating Arrays from Python Lists

# 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d)

# 2D array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

# 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)

# Special Array Creation Functions
# Array of zeros
zeros = np.zeros((3, 4))  # 3 rows, 4 columns
print(zeros)

# Array of ones
ones = np.ones((2, 3, 4), dtype=np.int16)  # 2x3x4 array of 1's
print(ones)

# Empty array (contains garbage values)
empty = np.empty((2, 3))
print(empty)

# Identity matrix
identity = np.eye(3)  # 3x3 identity matrix
print(identity)

# Array with a range of values
range_arr = np.arange(10, 30, 5)  # from 10 to 30 (exclusive), step 5
print(range_arr)

# Array with evenly spaced numbers
linspace_arr = np.linspace(0, 2, 9)  # 9 numbers from 0 to 2
print(linspace_arr)

# Array Attributes
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.ndim)    # Number of dimensions (2)
print(arr.shape)   # Tuple of array dimensions (2, 3)
print(arr.size)    # Total number of elements (6)
print(arr.dtype)   # Data type of elements (int64)
print(arr.itemsize) # Size in bytes of each element (8)
print(arr.nbytes)  # Total bytes consumed by elements (48)

# Array Indexing and Slicing
# Basic Indexing
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[2])    # Get element at index 2 (2)
print(arr[-1])   # Last element (9)

# For multidimensional arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[1, 2])  # Row 1, column 2 (6)

# Slicing
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[1:5])    # Elements from index 1 to 4 [1, 2, 3, 4]
print(arr[::2])    # Every second element [0, 2, 4, 6, 8]
print(arr[::-1])   # Reversed array [9, 8, ..., 0]

# Multidimensional slicing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[:2, 1:])  # First two rows, columns from 1 onward

# Boolean Indexing
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Create boolean array
filter = arr > 5
print(filter)  # [False, False, False, False, False, True, True, True, True]

# Use boolean array to filter
print(arr[filter])  # [6, 7, 8, 9]

# Shorter syntax
print(arr[arr > 5])  # Same as above

# Array Operations
# Arithmetic Operations

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5, 7, 9]
print(a - b)   # [-3, -3, -3]
print(a * b)   # [4, 10, 18] (element-wise multiplication)
print(a / b)   # [0.25, 0.4, 0.5]
print(a ** 2)  # [1, 4, 9]
print(np.sqrt(a))  # [1., 1.4142, 1.73205]

# Matrix Operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
print(np.dot(a, b))
# or
print(a @ b)

# Transpose
print(a.T)

# Inverse
print(np.linalg.inv(a))

# Determinant
print(np.linalg.det(a))

# Comparison Operations
a = np.array([1, 2, 3])
b = np.array([2, 2, 2])

print(a == b)  # [False, True, False]
print(a > b)   # [False, False, True]
print(np.array_equal(a, b))  # False

# Broadcasting
# Broadcasting allows NumPy to perform operations on arrays of different shapes.
a = np.array([1, 2, 3])
b = 2

print(a * b)  # [2, 4, 6] - b is broadcast to array of same shape as a

# More complex example
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([1, 0, 1])

print(a + b)  # b is broadcast to each row of a

# Array Manipulation
# Changing Array Shape

arr = np.arange(6)
print(arr.reshape(2, 3))  # Reshape to 2x3 array

# Flatten array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d.flatten())  # [1, 2, 3, 4, 5, 6]

# Stacking Arrays

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack((a, b)))  # Vertical stack
print(np.hstack((a, b)))  # Horizontal stack
print(np.column_stack((a, b)))  # Column stack

# Splitting Arrays
arr = np.arange(9).reshape(3, 3)
print(np.hsplit(arr, 3))  # Split into 3 arrays along horizontal axis
print(np.vsplit(arr, 3))  # Split into 3 arrays along vertical axis

# Mathematical Functions
arr = np.array([1, 2, 3, 4])

print(np.sum(arr))       # Sum of all elements (10)
print(np.prod(arr))      # Product of all elements (24)
print(np.mean(arr))      # Mean (2.5)
print(np.std(arr))       # Standard deviation
print(np.var(arr))       # Variance
print(np.min(arr))       # Minimum value (1)
print(np.max(arr))       # Maximum value (4)
print(np.argmin(arr))    # Index of minimum value (0)
print(np.argmax(arr))    # Index of maximum value (3)
print(np.cumsum(arr))    # Cumulative sum [1, 3, 6, 10]
print(np.cumprod(arr))   # Cumulative product [1, 2, 6, 24]

# Linear Algebra
a = np.array([[1, 2], [3, 4]])

# Matrix rank
print(np.linalg.matrix_rank(a))

# Eigenvalues and eigenvectors
print(np.linalg.eig(a))

# Solve linear equations
# 3x + y = 9
# x + 2y = 8
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
print(np.linalg.solve(A, b))  # Solution [2., 3.]

# Singular Value Decomposition
print(np.linalg.svd(a))

# Statistics
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(np.median(arr))        # Median of all elements
print(np.percentile(arr, 50)) # 50th percentile (same as median)
print(np.corrcoef(arr))      # Correlation coefficient matrix
print(np.histogram(arr))     # Histogram

# Random Module
# NumPy's random module allows you to generate random numbers:
# Random float between 0 and 1
print(np.random.random())

# Random integers between low and high
print(np.random.randint(1, 10, size=5))  # 5 random integers between 1 and 9

# Random choice from array
print(np.random.choice(['a', 'b', 'c'], size=10))

# Standard normal distribution
print(np.random.randn(2, 3))  # 2x3 array of standard normal values

# Shuffle array
arr = np.arange(10)
np.random.shuffle(arr)
print(arr)

# File I/O
# Saving and Loading Arrays

arr = np.arange(10)

# Save to binary file
np.save('my_array.npy', arr)

# Load from binary file
loaded = np.load('my_array.npy')
print(loaded)

# Save to text file
np.savetxt('my_array.txt', arr)

# Load from text file
loaded_txt = np.loadtxt('my_array.txt')
print(loaded_txt)

# Working with CSV Files
# Save array to CSV
arr = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('my_array.csv', arr, delimiter=',')

# Load CSV into array
loaded_csv = np.loadtxt('my_array.csv', delimiter=',')
print(loaded_csv)


