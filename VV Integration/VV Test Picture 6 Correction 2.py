def update(frame, particles, scatters):
    update_acceleration(particles)
    update_velocity(particles, dt)
    for p in particles:
        p.update_position(dt)
      
    for p, scatter in zip(particles, scatters):
        scatter.set_offsets(p.position)
        scatter.set_color(p.color)
    return scatters
