import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as Animation


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

omegaConstant = 1
numMasses = matrixSize
#egienValues are here
#eigneVectors are here
x_space = 1
initalMassX_values = [0 for _ in range(numMasses)]

#Sets up masses x points with a spacing of 1
for i in range(len(initalMassX_values)):
    initalMassX_values[i] = (i-50) * x_space

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

#multiplying the egen vector by the omega
funcOmegas = egVec * omegaConstant

#
normal_mode_amps = [0 for i in range(matrixSize)]
normal_mode_amps[49] = 1
print(normal_mode_amps)

massArray = [0 for _ in range(numMasses)]


for i in range(numMasses):
    massArray[i] = ax.plot([], [], 'o', markersize=10)


def update(frame):
    t = frame * dt
    for i in range(numMasses):
        x = initalMassX_values[i]
        for omega, mode, amplitude in zip(funcOmegas, egVec, normal_mode_amps):
            x += amplitude*mode[i]*np.cos(omega*t) 
    
        massArray[i].set_data([x], [0])
    return massArray

# Create animation
Animation(fig, update, frames=num_frames, blit=True)

# Show plot
plt.xlabel('Position')
plt.ylabel('Height')
plt.title('Masses Oscillation')
plt.grid(True)
plt.show()
