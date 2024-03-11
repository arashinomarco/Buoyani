import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Particle:
    def __init__(self, color):
        self.color = color
        self.position = np.random.rand(2) * 10 - 5
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

    for p, scatter in zip(particles, scatters):
        scatter.set_offsets(p.position)
        scatter.set_color(p.color)
    return scatters

dt = 0.1
total_time = 10
particles = init_particles()
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.grid(True)

scatters = [ax.scatter(p.position[0], p.position[1], c=p.color) for p in particles]
ref_point = ax.scatter(0, 0, c='y')
theta = np.linspace(np.pi/2, -np.pi/2, 100)
x_circle = -2 * np.cos(theta)
y_circle = 2 * np.sin(theta)
ax.fill_betweenx(y_circle, x_circle, -5, color='gray')
num_frames = int(total_time / dt)
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(particles, scatters), blit=True)

plt.show()
