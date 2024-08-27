import numpy as np

# Create a 2D array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Get the length of the first axis (number of rows)
length_first_axis = len(array)
print("Length of the first axis (number of rows):", length_first_axis)

# Get the total number of elements in the array
total_elements = np.size(array)
print("Total number of elements:", total_elements)

# Get the shape of the array
shape = np.shape(array)
print("Shape of the array (rows, columns):", shape)

# Optionally, get the number of rows and columns separately
num_rows, num_columns = shape
print("Number of rows:", num_rows)
print("Number of columns:", num_columns)
