import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

class Particle:
    def __init__(self, color):
        self.color = color
        self.position = np.random.rand(2) * 9 - 4.5
        self.velocity = np.random.rand(2) * 2 - 1
        self.acceleration = np.zeros(2)

def update_velocity(particles, dt):
    for p in particles:
        p.velocity += p.acceleration * dt / 2

def update_position(particles, dt):
    for p in particles:
        p.position += p.velocity * dt

def update_acceleration(particles):
    for p in particles:
        p.acceleration = np.random.rand(2) * 2 - 1

def init_particles():
    particles = [Particle('g') for _ in range(10)]
    particles.extend([Particle('r') for _ in range(15)])
    return particles

def update(frame, particles, scatters):
    update_acceleration(particles)
    update_velocity(particles, dt)
    update_position(particles, dt)
    
    # Update scatter plot data
    for p, scatter in zip(particles, scatters):
        scatter.set_offsets(p.position)
        scatter.set_color(p.color)
    return scatters

dt = 0.1
total_time = 10
image_path = 
image = plt.imread(image_path)
image_extent = [-image.shape[1] / 2 + 500, image.shape[1] / 2 + 500, -image.shape[0] / 2, image.shape[0] / 2]

fig, ax = plt.subplots()
ax.imshow(image, extent=image_extent)
ax.set_xlim(image_extent[:2])
ax.set_ylim(image_extent[2:])

particles = init_particles()
scatters = [ax.scatter(p.position[0], p.position[1], c=p.color) for p in particles]
num_frames = int(total_time / dt)
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(particles, scatters), blit=True)
ani.save('particle_animation.mp4', fps=30)

plt.show()
