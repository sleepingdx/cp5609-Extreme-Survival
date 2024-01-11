import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置窗口大小
window_size = (960, 720)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Game Over")

# 加载背景图像
background_image = pygame.image.load("E:/jcu/Extreme Survival/res/Background/gameover.jpg")
background_rect = background_image.get_rect()

# 设置字体
font = pygame.font.Font(None, 36)

# 设置按钮
button_width = 140
button_height = 50
button_spacing = 20
retry_button = pygame.Rect(170, 600, button_width, button_height)
quit_button = pygame.Rect(650, 600, button_width, button_height)

# 循环标志
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if retry_button.collidepoint(event.pos):
                # 在这里添加跳回最初界面的逻辑
                pass
            elif quit_button.collidepoint(event.pos):
                running = False

    # 绘制背景
    screen.blit(background_image, background_rect)

    # 绘制按钮
    pygame.draw.rect(screen, (0, 255, 0), retry_button)
    pygame.draw.rect(screen, (255, 0, 0), quit_button)

    # 绘制按钮上的文本
    retry_text = font.render("Retry", True, (255, 255, 255))
    quit_text = font.render("Quit", True, (255, 255, 255))
    screen.blit(retry_text, (retry_button.x + 45, retry_button.y + 15))
    screen.blit(quit_text, (quit_button.x + 45, quit_button.y + 15))

    # 更新屏幕
    pygame.display.flip()

# 退出Pygame
pygame.quit()
sys.exit()