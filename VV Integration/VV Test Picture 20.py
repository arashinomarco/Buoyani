import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Particle:
    def __init__(self, color, xlim, ylim, image_extent):
        self.color = color
        self.position = self.random_position(xlim, ylim, image_extent)
        self.velocity = np.random.rand(2) * 10 - 5

    def random_position(self, xlim, ylim, image_extent):
        while True:
            position = np.random.rand(2) * (xlim[1] - xlim[0]) + xlim[0], np.random.rand(2) * (ylim[1] - ylim[0]) + ylim[0]
            if not (image_extent[0] <= position[0] <= image_extent[1]) and (image_extent[2] <= position[1] <= image_extent[3]):
                return position

def update(frame, particles, scatters, yellow_dot_position):
    acceleration_directions = yellow_dot_position - particles[:, :2]
    acceleration_magnitudes = 30  # kph
    accelerations = (acceleration_directions / np.linalg.norm(acceleration_directions, axis=1)[:, None]) * (acceleration_magnitudes / 3.6) * dt
  
    particles[:, 2:] += accelerations * dt / 2
    particles[:, :2] += particles[:, 2:] * dt
    particles[:, 2:] = np.clip(particles[:, 2:], -145, 145)  # Limit velocity
    particles[:, :2] = np.clip(particles[:, :2], [xlim[0], ylim[0]], [xlim[1], ylim[1]])

    for i, scatter in enumerate(scatters):
        scatter.set_offsets(particles[i, :2])
        scatter.set_color(colors[i])

def init_particles(n, colors, xlim, ylim, image_extent):
    particles = np.zeros((n, 4))
    particles[:, :2] = np.random.rand(n, 2) * [xlim[1] - xlim[0], ylim[1] - ylim[0]] + [xlim[0], ylim[0]]
    particles[:, 2:] = np.random.rand(n, 2) * 10 - 5
    while True:
        indices = np.where(
            (image_extent[0] <= particles[:, 0]) & (particles[:, 0] <= image_extent[1]) &
            (image_extent[2] <= particles[:, 1]) & (particles[:, 1] <= image_extent[3])
        )[0]
        if len(indices) == 0:
            break
        particles[indices, :2] = np.random.rand(len(indices), 2) * [xlim[1] - xlim[0], ylim[1] - ylim[0]] + [xlim[0], ylim[0]]
    return particles

dt = 0.1
total_time = 10
particle_count = 30
image_path = '10173495_595562673884502_1007274173_n_595562670551169.png'
image = plt.imread(image_path)
image_extent = [0, image.shape[1] / image.shape[0] * 2000, -1000, 1000]
xlim = (-2000, 2000)
ylim = (-1000, 1000)
fig, ax = plt.subplots()
ax.imshow(image, extent=image_extent, aspect='auto', origin='upper')
ax.set_xlim(-2000, 2000)
ax.set_ylim(-1000, 1000)
colors = np.random.choice(['g', 'r'], particle_count)
particles = init_particles(particle_count, colors, xlim, ylim, image_extent)
yellow_dot_position = np.array([0, 0])
ax.scatter(yellow_dot_position[0], yellow_dot_position[1], c='yellow', zorder=10)
scatters = [ax.scatter(particles[i, 0], particles[i, 1], c=colors[i]) for i in range(particle_count)]
ani = animation.FuncAnimation(fig, update, frames=int(total_time / dt), fargs=(particles, scatters, yellow_dot_position), interval=dt*1000)
ani.save('particle_animation.mp4', fps=30)

plt.show()
