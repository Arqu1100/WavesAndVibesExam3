import numpy as np
import matplotlib.pyplot as plt


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

#### Constants of system ####

numMasses = matrixSize
#egienValues are here
#eigneVectors are here
x_space = 1
initalMassX_values = [0 for _ in range(numMasses)]

for i in range(len(initalMassX_values)):
    initalMassX_values[i] = (i-50) * x_space


print(initalMassX_values)
# Time parameters
t0 = 0
t_end = 1000
num_frames = 10000
t_values = np.linspace(t0, t_end, num_frames)
dt = (t_end - t0) / num_frames

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(-0.5, 0.5)



