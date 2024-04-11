import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#%matplotlib notebook

# Parameters
num_masses = 3
mass_radius = 0.1
omega0 = 1
spring_constant = 1
normal_mode_amps = [0, 1, 0]
normal_modes = [[-1,0,1], [1, np.sqrt(2), 1], [1, -np.sqrt(2), 1]]
omegas = [np.sqrt(2)*omega0, np.sqrt(2 + np.sqrt(2))*omega0, np.sqrt(2 - np.sqrt(2))*omega0]
initial_position = [-0.5, 0, 0.5]
initial_velocity = [0, 0, 0]

# Time parameters
t0 = 0
t_end = 100
num_frames = 1000
t_values = np.linspace(t0, t_end, num_frames)
dt = (t_end - t0) / num_frames

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 0.5)

# Initialize masses
mass1, = ax.plot([], [], 'o', markersize=10)
mass2, = ax.plot([], [], 'o', markersize=10)
mass3, = ax.plot([], [], 'o', markersize=10)

masses = [mass1, mass2, mass3]

# Update function
def update(frame):
    t = frame * dt
    for i in range(num_masses):
        x = initial_position[i]
        for omega, mode, amplitude in zip(omegas, normal_modes, normal_mode_amps):
            x += amplitude*mode[i]*np.cos(omega*t)
    
        masses[i].set_data([x], [0])
    return masses

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, blit=True)

# Show plot
plt.xlabel('Position')
plt.ylabel('Height')
plt.title('Masses Oscillation')
plt.grid(True)
plt.show()
