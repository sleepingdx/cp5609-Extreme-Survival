import pygame
import sys
import os
import subprocess

from codes import MyDefine

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
font_button = pygame.font.Font(None, 36)
font_text = pygame.font.Font(None, 80)

# 获取背景图像的路径，使用原始字符串
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取上一级目录的路径
parent_dir = os.path.dirname(current_dir)
# 获取上一级目录的路径
cur_path = MyDefine.get_current_path()
background_path = os.path.join(cur_path, "res/background/chara_selected.png")

# 加载背景图像
background_image = pygame.image.load(background_path)


# 函数：显示文本
def draw_text(text, x, y, color=black):
    text_surface = font_text.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def draw_button(text, x, y, color=black):
    text_surface = font_button.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


# 主循环
running = True
character_selected = None  # 存储选择的角色

while running:
    warrior_button_rect = pygame.Rect(width // 4 - 100, 600, 200, 50)
    archer_button_rect = pygame.Rect(width - (width // 4 + 150), 600, 200, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 构建 main.py 的相对路径
            cur_path = MyDefine.get_current_path()
            main_py = os.path.normpath(os.path.join(cur_path, "main.py"))
            if warrior_button_rect.collidepoint(event.pos):
                pygame.quit()
                character_selected = "Warrior"
                args_to_pass = ['0']
                subprocess.run(["python", main_py] + args_to_pass)
                print("Selected Warrior")
                sys.exit()
            elif archer_button_rect.collidepoint(event.pos):
                pygame.quit()
                character_selected = "Archer"
                args_to_pass = ['1']
                subprocess.run(["python", main_py] + args_to_pass)
                print("Selected Archer")
                sys.exit()

    # 清屏
    screen.fill(white)

    # 绘制背景图像
    screen.blit(background_image, (0, 0))
    # 显示标题
    draw_text("Character Selection", width // 2, 50)

    # 创建按钮
    pygame.draw.rect(screen, white, warrior_button_rect)
    draw_button("Warrior", warrior_button_rect.centerx, warrior_button_rect.centery, black)

    pygame.draw.rect(screen, white, archer_button_rect)
    draw_button("Archer", archer_button_rect.centerx, archer_button_rect.centery, black)

    # 更新屏幕
    pygame.display.flip()

# 在这里可以根据选择的角色进行相应的处理，例如加载不同的角色资源等

# 退出Pygame
pygame.quit()
sys.exit()
