import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Particle:
    def __init__(self, color, xlim, ylim, image_extent, particles_positions):
        self.color = color
        self.position = self.random_position(xlim, ylim, image_extent, particles_positions)
        self.velocity = np.random.rand(2) * 10 - 5
        self.acceleration = np.zeros(2)
        self.xlim = xlim
        self.ylim = ylim
        self.image_extent = image_extent

    def random_position(self, xlim, ylim, image_extent, particles_positions):
        while True:
            position = np.random.rand(2) * (xlim[1] - xlim[0]) + xlim[0], np.random.rand(2) * (ylim[1] - ylim[0]) + ylim[0]
            if not any((image_extent[0] <= pos[0] <= image_extent[1]) and (image_extent[2] <= pos[1] <= image_extent[3]) for pos in position):
                if not any(np.linalg.norm(np.array(position) - np.array(p)) < 100 for p in particles_positions):
                    return position

    def update_velocity(self, dt):
        self.velocity += self.acceleration * dt / 2

    def update_position(self, dt):
        new_position = self.position + self.velocity * dt
        mask = (new_position[0] >= self.xlim[0]) & (new_position[0] <= self.xlim[1]) & (new_position[1] >= self.ylim[0]) & (new_position[1] <= self.ylim[1])
        mask &= (new_position[0] >= self.image_extent[0]) & (new_position[0] <= self.image_extent[1]) & (new_position[1] >= self.image_extent[2]) & (new_position[1] <= self.image_extent[3])
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
image_extent = [0, image.shape[1] / 2, -image.shape[0] / 4, image.shape[0] / 4]
xlim = (-1400, 1400)
ylim = (-image.shape[0] / 4, image.shape[0] / 4)
fig, ax = plt.subplots()
ax.imshow(image, extent=image_extent)
ax.set_xlim(-1400, 1400)
ax.set_ylim(-image.shape[0] / 4, image.shape[0] / 4)
particles_positions = []
particles = [Particle('g', xlim, ylim, image_extent, particles_positions) for _ in range(10)]
particles_positions.extend(p.position for p in particles)
particles.extend([Particle('r', xlim, ylim, image_extent, particles_positions) for _ in range(15)])
particles_positions.extend(p.position for p in particles[len(particles)//2:])
ax.scatter(0, 0, c='yellow', zorder=10)
scatters = [ax.scatter(p.position[0], p.position[1], c=p.color) for p in particles]
num_frames = int(total_time / dt)
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(particles, scatters), blit=True)
ani.save('particle_animation.mp4', fps=30)

plt.show()
