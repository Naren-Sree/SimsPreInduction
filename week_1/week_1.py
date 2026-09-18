import pygame
import numpy as np
import random

# Configuration

WIDTH = 800
HEIGHT = 800

BOWL_CENTER = np.array([WIDTH / 2, HEIGHT / 2], dtype=float)
BOWL_RADIUS = 300

# Start with 1 ball, then 2. Many at once is the bonus.
NUM_PARTICLES = 20
PARTICLE_RADIUS = 10
PARTICLE_SPEED = 150.0

# Pixels per second squared, not m/s^2. Note that +y points DOWN on screen.
GRAVITY = 900.0

# How much speed survives a bounce. 1.0 loses nothing, below 1.0 is weaker.
WALL_RESTITUTION = 1.0
RESTITUTION = 1.0

FPS = 60

positions = []
velocities = []

for i in range(NUM_PARTICLES):

    # A random spot inside the bowl, with the whole ball fitting.
    angle = random.uniform(0, 2 * np.pi)
    distance = random.uniform(0, BOWL_RADIUS - PARTICLE_RADIUS)

    positions.append(BOWL_CENTER + distance * np.array([
        np.cos(angle),
        np.sin(angle)
    ]))

    # A random direction, at roughly PARTICLE_SPEED.
    # Swap for np.array([0.0, 0.0]) to drop the ball from rest.
    angle = random.uniform(0, 2 * np.pi)

    velocities.append(PARTICLE_SPEED * np.array([
        np.cos(angle),
        np.sin(angle)
    ]))
'''

    positions.append(BOWL_CENTER.copy()) 
    velocities.append(np.array([0.0, 0.0]))
'''
# Pygame setup

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulation")

clock = pygame.time.Clock()

running = True

# Main loop

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Seconds since the last frame. This is your timestep.
    dt = clock.tick(FPS) / 1000.0

    ###########################################################################
    # TODO: Make every ball fall, and bounce it off the wall of the bowl.     #
    ###########################################################################

    # CODE STARTS HERE.

    for i in range(NUM_PARTICLES):

        velocities[i] += np.array([0.0, GRAVITY]) * dt
        positions[i] += velocities[i] * dt

        d = positions[i] - BOWL_CENTER
        distance = np.linalg.norm(d)

        if distance > BOWL_RADIUS - PARTICLE_RADIUS:

            n = d / distance
            offset = distance - (BOWL_RADIUS - PARTICLE_RADIUS)
            positions[i] -= n * offset

            velocities[i] -= (1 + WALL_RESTITUTION) * np.dot(velocities[i], n) * n

    ###########################################################################
    #                            END OF YOUR CODE                             #
    ###########################################################################

    ###########################################################################
    # TODO: Make the balls bounce off each other.                             #
    ###########################################################################

    # CODE STARTS HERE.

    for i in range(NUM_PARTICLES):
        for j in range(i + 1, NUM_PARTICLES):

            d = positions[i] - positions[j]
            distance = np.linalg.norm(d)

            if distance == 0 or distance >= 2 * PARTICLE_RADIUS:
                continue

            n = d / distance

            delta = 2 * PARTICLE_RADIUS - distance
            positions[i] += n * (delta / 2)
            positions[j] -= n * (delta / 2)

            vn = np.dot(velocities[i] - velocities[j], n)

            if vn >= 0:
                continue

            velocities[i] -= 0.5 * (1 + RESTITUTION) * vn * n
            velocities[j] += 0.5 * (1 + RESTITUTION) * vn * n

    ###########################################################################
    #                            END OF YOUR CODE                             #
    ###########################################################################

    # Render

    screen.fill((20, 20, 25))

    pygame.draw.circle(
        screen,
        (180, 180, 180),
        BOWL_CENTER.astype(int),
        BOWL_RADIUS,
        width=3
    )

    for position in positions:
        pygame.draw.circle(
            screen,
            (220, 220, 220),
            position.astype(int),
            PARTICLE_RADIUS
        )

    pygame.display.flip()

pygame.quit()