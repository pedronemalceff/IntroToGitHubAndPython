import numpy as np
print('Question 1')
matrix = np.eye(3)
print(matrix)
print()

print('Question 2')
matrix[matrix == 0] += 3
print(matrix)
print()

print('Question 3')
matrix = np.delete(matrix, -1, axis=1)
print(matrix)


