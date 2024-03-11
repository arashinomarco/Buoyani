def update_acceleration(particles, yellow_dot_position):
    for p in particles:
        distance_to_yellow_dot = np.linalg.norm(p.position - yellow_dot_position)
        if distance_to_yellow_dot < 100:
            acceleration_direction = yellow_dot_position - p.position
            acceleration_magnitude = 30
            acceleration = (acceleration_direction / np.linalg.norm(acceleration_direction)) * (acceleration_magnitude / 3.6) * dt
            p.velocity += acceleration
