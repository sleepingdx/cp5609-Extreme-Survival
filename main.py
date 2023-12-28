import pygame

# 初始化Pygame
pygame.init()

# 设置窗口尺寸
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("My 2D Game")

# 游戏循环
running = True
while running:
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充窗口为白色
    win.fill((255, 255, 255))

    # 在窗口上绘制一些图形或精灵
    # 这里可以添加你自己的绘制逻辑，比如绘制角色、地图、物体等

    # 刷新屏幕
    pygame.display.flip()

# 退出Pygame
pygame.quit()
