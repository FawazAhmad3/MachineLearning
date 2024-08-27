import numpy as np

array_1d = np.array([10, 20, 30, 40, 50, 60])

slice_1d = array_1d[1:4]
print("Sliced 1D array:", slice_1d)


array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12]])


slice_2d = array_2d[:2, 2:]
print("Sliced 2D array:\n", slice_2d)


second_row = array_2d[1, :]
print("Second row:", second_row)


third_column = array_2d[:, 2]
print("Third column:", third_column)
