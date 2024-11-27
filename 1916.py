import pygame
import random
import sys

# Khởi tạo pygame
pygame.init()

# Cấu hình màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chúc mừng sinh nhật Michelle")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (218, 165, 32)

# Phông chữ hỗ trợ tiếng Nhật
FONT_PATH = "NotoSansJP-VariableFont_wght.ttf"  # Đảm bảo phông chữ này có trong thư mục dự án
font_large = pygame.font.Font(FONT_PATH, 50)
font_small = pygame.font.Font(FONT_PATH, 30)

# Phát bài hát
pygame.mixer.init()
pygame.mixer.music.load("em_xinh.mp3")  # Đảm bảo tệp âm thanh nằm trong thư mục dự án
pygame.mixer.music.play(-1)  # Phát lặp lại vô hạn

# Hiệu ứng pháo hoa
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = [
            [x, y, random.randint(-5, 5), random.randint(-5, 5), random.randint(2, 4)]
            for _ in range(50)
        ]

    def draw(self, screen):
        for particle in self.particles:
            pygame.draw.circle(screen, GOLD, (int(particle[0]), int(particle[1])), particle[4])

    def update(self):
        for particle in self.particles:
            particle[0] += particle[2]
            particle[1] += particle[3]
            particle[4] -= 0.1

        self.particles = [p for p in self.particles if p[4] > 0]

fireworks = []

# Hiển thị thông điệp
messages = [
    "Chúc mừng sinh nhật Michelle!",
    "\u30DF\u30C3\u30B7\u30A7\u30EB\u3055\u3093\u304A\u8A95\u751F\u65E5\u304A\u3081\u3067\u3068\u3046!",  # Tiếng Nhật
    "Happy Birthday, Michelle!"
]

# Vòng lặp chính
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    # Hiển thị thông điệp
    y_offset = HEIGHT // 3
    for msg in messages:
        text_surface = font_large.render(msg, True, WHITE)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, y_offset))
        y_offset += 70

    # Cập nhật pháo hoa
    for firework in fireworks:
        firework.update()
        firework.draw(screen)

    # Lắng nghe sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            fireworks.append(Firework(x, y))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
