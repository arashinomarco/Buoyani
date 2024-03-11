def random_position(self, xlim, ylim, image_extent, particles_positions):
    while True:
        position = np.random.rand(2) * (xlim[1] - xlim[0]) + xlim[0], np.random.rand(2) * (ylim[1] - ylim[0]) + ylim[0]
        if not any((image_extent[0] <= pos[0] <= image_extent[1]) and (image_extent[2] <= pos[1] <= image_extent[3]) for pos in position):
            if not any(np.linalg.norm(np.array(position) - np.array(p)) < 100 for p in particles_positions):
                return position
