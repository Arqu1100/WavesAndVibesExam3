import numpy as np



#matrix size constant
matrixSize = 100

#
omega = 5

w_0 = 1

#creats a new matrix of size select in matrixSize and a unit matrix of the same size
def createMatrix(matrixSize, omega, w_0):
    matrix = [[0 for _ in range(matrixSize)] for _ in range(matrixSize)]
    unitMatrix = np.eye(matrixSize) * omega

    for i in range(matrixSize):
        matrix[i][i] = 2*w_0**2
    
    for i in range(1,matrixSize):
        matrix[i][i - 1] = -w_0 ** 2
        matrix[i-1][i] = -w_0 ** 2

    
    return matrix

npMatrix = createMatrix(matrixSize, omega , w_0)

egVal, egVec = np.linalg.eig(npMatrix)

print("EigenValues:", egVal)
print("Eigen Vectors:", egVec)

