# Generates a matrix of size x and returns its eigenvectors and eigenvalues
import numpy as np
from sympy import Matrix

def create_matrix(size, w_0):
    # Create an empty matrix
    matrix = Matrix([[0]*size for _ in range(size)])

    # Fill the diagonal with 2w_0^2
    for i in range(size):
        matrix[i, i] = 2 * w_0 ** 2

    # Fill the elements surrounding the diagonal with -w_0^2
    for i in range(1, size):
        matrix[i, i-1] = -w_0 ** 2
        matrix[i-1, i] = -w_0 ** 2

    return matrix

# Define the size of the matrix and w_0
matrix_size = 100
w_0 = 1.0  # You can set this to any value you want

# Create the matrix
matrix = create_matrix(matrix_size, w_0)

# Convert SymPy matrix to NumPy array
matrix_np = np.array(matrix.tolist(), dtype=float)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix_np)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)