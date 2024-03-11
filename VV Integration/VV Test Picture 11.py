import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Particle:
    def __init__(self, color, xlim, ylim):
        self.color = color
        self.position = np.random.rand(2) * (xlim[1] - xlim[0]) + xlim[0], np.random.rand(2) * (ylim[1] - ylim[0]) + ylim[0]
        self.velocity = np.random.rand(2) * 500 - 1
        self.acceleration = np.zeros(2)
        self.xlim = xlim
        self.ylim = ylim

    def update_velocity(self, dt):
        self.velocity += self.acceleration * dt / 2

    def update_position(self, dt):
        new_position = self.position + self.velocity * dt
        mask = (new_position[0] >= self.xlim[0]) & (new_position[0] <= self.xlim[1]) & (new_position[1] >= self.ylim[0]) & (new_position[1] <= self.ylim[1])
        self.position = np.where(mask[:, None], new_position, self.position)

def update(frame, particles, scatters):
    update_acceleration(particles)
    update_velocity(particles, dt)
    for p in particles:
        p.update_position(dt)
      
    for p, scatter in zip(particles, scatters):
        scatter.set_offsets(p.position)
        scatter.set_color(p.color)
    return scatters

def update_acceleration(particles):
    pass

def update_velocity(particles, dt):
    pass

dt = 0.1
total_time = 10
image_path = '10173495_595562673884502_1007274173_n_595562670551169.png'
image = plt.imread(image_path)
image_extent = [-1400, 1400, -image.shape[0] / 4, image.shape[0] / 4]
xlim = (-1400, 1400)
ylim = (-image.shape[0] / 4, image.shape[0] / 4)
fig, ax = plt.subplots()
ax.imshow(image, extent=image_extent)
ax.set_xlim(image_extent[:2])
ax.set_ylim(image_extent[2:])
particles = [Particle('g', xlim, ylim) for _ in range(10)]
particles.extend([Particle('r', xlim, ylim) for _ in range(15)])
scatters = [ax.scatter(p.position[0], p.position[1], c=p.color) for p in particles]
num_frames = int(total_time / dt)
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(particles, scatters), blit=True)
ani.save('particle_animation.mp4', fps=30)

plt.show()
