import os

import pygame
import sys

# 初始化Pygame
pygame.init()

# 窗口大小
width, height = 960, 720
screen = pygame.display.set_mode((width, height))

# 设置窗口标题
pygame.display.set_caption("Extreme Survival")

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# 字体设置为默认字体
font_button = pygame.font.Font(None, 36)
font_text = pygame.font.Font(None, 100)


# 函数：显示文本
def draw_text(text, x, y, color=white):
    text_surface = font_text.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def draw_button(text, x, y, color=black):
    text_surface = font_button.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


# 获取背景图像的路径，使用原始字符串
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取上一级目录的路径
if getattr(sys, 'frozen', False):
    # 当程序被打包成exe文件时
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(current_dir)
background_path = os.path.join(base_path, r"res\Background\Startpage.png")

# 加载背景图像
background_image = pygame.image.load(background_path)
# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                # 进入角色选择界面
                character_choose = True
            elif exit_button_rect.collidepoint(event.pos):
                running = False

    # 清屏
    screen.fill(white)
    # 绘制背景图像
    screen.blit(background_image, (0, 0))

    # 显示标题
    draw_text("Extreme Survival", width // 2, 120)

    # 创建按钮
    start_button_rect = pygame.Rect(width // 2 - 100, 300, 200, 50)
    pygame.draw.rect(screen, green, start_button_rect)

    # 显示按钮上的文字
    draw_button("Start", start_button_rect.centerx, start_button_rect.centery, black)

    exit_button_rect = pygame.Rect(width // 2 - 100, 400, 200, 50)
    pygame.draw.rect(screen, green, exit_button_rect)
    draw_button("Exit", width // 2, 425, black)

    # 更新屏幕
    pygame.display.flip()

# 退出Pygame
pygame.quit()
sys.exit()
