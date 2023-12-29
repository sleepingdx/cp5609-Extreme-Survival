import pygame
import sys

# 初始化Pygame
pygame.init()

# 窗口大小
width, height = 960, 720
screen = pygame.display.set_mode((width, height))

# 设置窗口标题
pygame.display.set_caption("Character Selection")

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# 字体设置为默认字体
font = pygame.font.Font(None, 36)

# 函数：显示文本
def draw_text(text, x, y, color=black):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# 主循环
running = True
character_selected = None  # 存储选择的角色

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if warrior_button_rect.collidepoint(event.pos):
                character_selected = "Warrior"
                print("Selected Warrior")
            elif archer_button_rect.collidepoint(event.pos):
                character_selected = "Archer"
                print("Selected Archer")

    # 清屏
    screen.fill(white)

    # 显示标题
    draw_text("Character Selection", width // 2, 100)

    # 创建按钮
    warrior_button_rect = pygame.Rect(width // 2 - 100, 300, 200, 50)
    pygame.draw.rect(screen, green, warrior_button_rect)
    draw_text("Warrior", warrior_button_rect.centerx, warrior_button_rect.centery, black)

    archer_button_rect = pygame.Rect(width // 2 - 100, 400, 200, 50)
    pygame.draw.rect(screen, green, archer_button_rect)
    draw_text("Archer", archer_button_rect.centerx, archer_button_rect.centery, black)

    # 更新屏幕
    pygame.display.flip()

# 在这里可以根据选择的角色进行相应的处理，例如加载不同的角色资源等

# 退出Pygame
pygame.quit()
sys.exit()