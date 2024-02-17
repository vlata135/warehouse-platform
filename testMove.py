import pygame
import sys

class Agent:
    def __init__(self, start_cell, paths, color):
        self.paths = paths
        self.color = color
        self.path_index = 0
        self.speed = 2
        self.x, self.y = self.grid_to_pixel(*start_cell)

    def grid_to_pixel(self, x, y):
        return x * tile_size + tile_size // 2, y * tile_size + tile_size // 2

    def move(self):
        current_path = self.paths[self.path_index]

        if len(current_path) > 1:
            target_x, target_y = self.grid_to_pixel(*current_path[1])

            if self.x != target_x or self.y != target_y:
                direction_x = 1 if target_x > self.x else -1
                direction_y = 1 if target_y > self.y else -1

                self.x += self.speed * direction_x
                self.y += self.speed * direction_y
            else:
                # Nếu đã đến ô kế tiếp trong path, chuyển sang ô tiếp theo
                current_path.pop(0)

        else:
            # Nếu đã đi qua hết path hiện tại, chuyển sang path tiếp theo
            self.path_index = (self.path_index + 1) % len(self.paths)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), object_radius)

# Khởi tạo Pygame
pygame.init()

# Các thông số của grid và đối tượng
grid_size = 5
tile_size = 50
object_radius = 20

# Khởi tạo cửa sổ Pygame
screen_size = (grid_size * tile_size, grid_size * tile_size)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Moving Agent along Paths")

# Tạo danh sách các đường đi và tọa độ của từng ô
paths = [
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
    [(0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
]

# Tạo danh sách các agent
agents = [
    Agent((0, 0), paths, (255, 0, 0)),
    Agent((1, 1), paths, (0, 255, 0)),
    # Thêm các Agent khác tại đây...
]

# Vòng lặp chính
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for agent in agents:
        agent.move()

    # Vẽ lưới
    for i in range(grid_size):
        for j in range(grid_size):
            pygame.draw.rect(screen, (255, 255, 255), (i * tile_size, j * tile_size, tile_size, tile_size), 1)

    # Vẽ các đối tượng
    for agent in agents:
        agent.draw(screen)

    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(60)
