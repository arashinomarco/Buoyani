def update_acceleration(particles):
    pass

def update_velocity(particles, dt):
    for p in particles:
        acceleration = np.random.rand(2) * 2 - 1
        p.velocity += acceleration * dt
        speed = np.linalg.norm(p.velocity)
        if speed < 64:
            p.velocity = p.velocity / speed * 64
        elif speed > 145:
            p.velocity = p.velocity / speed * 145
