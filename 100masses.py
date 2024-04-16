import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

omegaConstant = 50

numMasses = matrixSize

#Spacing between objects
x_space = 2
initalMassX_values = [0 for _ in range(numMasses)]

#### ####

#Sets up masses x points with a spacing of 1
for i in range(len(initalMassX_values)):
    initalMassX_values[i] = (i-50) * x_space

# Time parameters
t0 = 0
t_end = 100000
num_frames = 1000000
t_values = np.linspace(t0, t_end, num_frames)
dt = (t_end - t0) / num_frames


#multiplying the egen vector by the omega
funcOmegas = egVal * omegaConstant

#Initializes normal modes
normal_mode_amps = [0 for i in range(matrixSize)]

#still needs work to make it more user friendly to select normal modes
normal_mode_amps[50] = 1
normal_mode_amps[25] = 1
normal_mode_amps[75] = 1
normal_mode_amps[80] = 1

massArray = []

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-110, 110)
ax.set_ylim(-0.2, 0.2)

#Creates a new array of 2D objects
for i in range(numMasses):
    massMark, = ax.plot([], [], 'o', markersize=3)
    massArray.append(massMark)
    


def update(frame):
    
    t = frame * dt
    for i in range(numMasses):
        x = initalMassX_values[i]
        for omega, mode, amplitude in zip(funcOmegas, egVec, normal_mode_amps):
            x += amplitude*mode[i]*np.cos(omega*t) 
            
        massArray[i].set_data([x],[0])
        
    return massArray

# Create animation
Animation = FuncAnimation(fig, update, frames=num_frames, blit=True)

# Show plot
plt.xlabel('Position')
plt.ylabel('Height')
plt.title('Masses Oscillation')
plt.grid(True)
plt.show()
