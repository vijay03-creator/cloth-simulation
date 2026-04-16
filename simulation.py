import pygame
import math

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cloth Simulation")

clock = pygame.time.Clock()

# Grid settings
cols, rows = 40, 30
spacing = 15

# Create points (x, y, old_x, old_y, pinned)
points = []
for y in range(rows):
    for x in range(cols):
        px = x * spacing + 100
        py = y * spacing + 50
        pinned = (y == 0)  # top row fixed
        points.append([px, py, px, py, pinned])

# Create constraints (connections)
constraints = []
for y in range(rows):
    for x in range(cols):
        i = x + y * cols

        if x < cols - 1:
            constraints.append((i, i + 1))

        if y < rows - 1:
            constraints.append((i, i + cols))


# Get distance between two points
def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


# Main loop
running = True
while running:
    screen.fill((10, 10, 20))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouse interaction
    mx, my = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]

    # Verlet Integration (movement)
    for p in points:
        if not p[4]:  # not pinned
            vx = (p[0] - p[2]) * 0.99
            vy = (p[1] - p[3]) * 0.99 + 0.3  # gravity

            p[2], p[3] = p[0], p[1]
            p[0] += vx
            p[1] += vy

            # Mouse pull effect
            if mouse_pressed:
                dist = math.hypot(p[0] - mx, p[1] - my)
                if dist < 80:
                    p[0] = mx
                    p[1] = my

    # Apply constraints multiple times (stability)
    for _ in range(5):
        for i1, i2 in constraints:
            p1 = points[i1]
            p2 = points[i2]

            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            dist = math.hypot(dx, dy)
            rest_length = spacing

            if dist == 0:
                continue

            diff = (dist - rest_length) / dist

            if not p1[4]:
                p1[0] += dx * 0.5 * diff
                p1[1] += dy * 0.5 * diff

            if not p2[4]:
                p2[0] -= dx * 0.5 * diff
                p2[1] -= dy * 0.5 * diff

    # Draw lines
    for i1, i2 in constraints:
        p1 = points[i1]
        p2 = points[i2]
        pygame.draw.line(screen, (0, 255, 150), (p1[0], p1[1]), (p2[0], p2[1]), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()