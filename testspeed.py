import pygame
import sys

pygame.init()

# Màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Object with Acceleration")

# Đối tượng
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.1  # Gia tốc
        self.max_speed = 5  # Tốc độ tối đa
        self.stopping_acceleration = 0.2  # Gia tốc khi dừng

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def apply_acceleration(self, direction_x, direction_y):
        self.velocity_x += self.acceleration * direction_x
        self.velocity_y += self.acceleration * direction_y

        # Giữ vững tốc độ tối đa
        speed = (self.velocity_x ** 2 + self.velocity_y ** 2) ** 0.5
        if speed > self.max_speed:
            factor = self.max_speed / speed
            self.velocity_x *= factor
            self.velocity_y *= factor

    def stop(self):
        # Gia tốc khi dừng
        self.velocity_x *= 1 - self.stopping_acceleration
        self.velocity_y *= 1 - self.stopping_acceleration

# Tạo đối tượng
player = GameObject(width // 2, height // 2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    direction_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    direction_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]

    player.apply_acceleration(direction_x, direction_y)
    player.update()

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (int(player.x), int(player.y)), 20)

    pygame.display.flip()
    clock.tick(60)

    # Khi nhấn space, dừng robot
    if keys[pygame.K_SPACE]:
        player.stop()
