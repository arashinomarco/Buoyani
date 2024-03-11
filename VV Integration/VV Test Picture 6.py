import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

class Particle:
    def __init__(self, color, xlim, ylim):
        self.color = color
        self.position = np.random.rand(2) * (xlim[1] - xlim[0]) + xlim[0], np.random.rand(2) * (ylim[1] - ylim[0]) + ylim[0]
        self.velocity = np.random.rand(2) * 2 - 1
        self.acceleration = np.zeros(2)
        self.xlim = xlim
        self.ylim = ylim

    def update_velocity(self, dt):
        self.velocity += self.acceleration * dt / 2

    def update_position(self, dt):
        new_position = self.position + self.velocity * dt
        if not (self.xlim[0] < new_position[0] < self.xlim[1] and self.ylim[0] < new_position[1] < self.ylim[1]):
            self.velocity *= -1  # Reverse direction if hitting the boundary
        self.position = self.position + self.velocity * dt

def update_particles(particles, dt):
    for p in particles:
        p.update_velocity(dt)
        p.update_position(dt)

def init_particles(num_particles, xlim, ylim):
    particles = [Particle('g', xlim, ylim) for _ in range(num_particles)]
    return particles

def update(frame, particles, scatters):
    update_particles(particles, dt)
    
    # Update scatter plot data
    for p, scatter in zip(particles, scatters):
        scatter.set_offsets(p.position)
        scatter.set_color(p.color)
    return scatters
  
dt = 0.1
total_time = 10
xlim = (500, 500 + 500)
ylim = (-250, 250)
num_particles = 25
image_path =
image = plt.imread(image_path)
image_extent = [xlim[0], xlim[1], ylim[0], ylim[1]]

fig, ax = plt.subplots()
ax.imshow(image, extent=image_extent)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

particles = init_particles(num_particles, xlim, ylim)
scatters = [ax.scatter(p.position[0], p.position[1], c=p.color) for p in particles]
num_frames = int(total_time / dt)
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(particles, scatters), blit=True)
ani.save('particle_animation.mp4', fps=30)

plt.show()
