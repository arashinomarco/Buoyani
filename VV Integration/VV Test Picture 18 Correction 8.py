def update_acceleration(particles, yellow_dot_position):
    for p in particles:
        acceleration_direction = yellow_dot_position - p.position
        acceleration_magnitude = 30  # kph
        acceleration = (acceleration_direction / np.linalg.norm(acceleration_direction)) * (acceleration_magnitude / 3.6) * dt
        acceleration = acceleration.reshape((1, 2))
        p.acceleration += acceleration
