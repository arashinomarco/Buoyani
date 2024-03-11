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
        mask = (self.xlim[0] < new_position[0]) & (new_position[0] < self.xlim[1]) & (self.ylim[0] < new_position[1]) & (new_position[1] < self.ylim[1])
        self.velocity[mask] *= -1
        self.position += self.velocity * dt
