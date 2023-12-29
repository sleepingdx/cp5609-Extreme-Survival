import pygame

# 初始化Pygame
pygame.init()

# 设置窗口尺寸
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Sprite with Keyframes")

# 加载包含多个关键帧的图像
keyframes_image = pygame.image.load('Actor1.png')  # 替换为你自己的包含关键帧的图像

# 定义关键帧大小和数量
frame_width = 48
frame_height = 48
num_frames_horizontal = keyframes_image.get_width() // frame_width

# 创建精灵类


class KeyframeSprite(pygame.sprite.Sprite):
    def __init__(self, frames, frame_index):
        super().__init__()
        self.frames = frames  # 存储所有关键帧的图像
        self.image = frames[frame_index]  # 设置当前精灵的图像
        self.rect = self.image.get_rect()
        self.rect.center = (win_width // 2, win_height // 2)  # 初始位置在窗口中心

    def update(self):
        # 这里可以添加精灵的更新逻辑
        pass


# 根据关键帧数量切分图像并保存每个关键帧的图像
frames_list = []
for i in range(num_frames_horizontal):
    left = i * frame_width
    frame_surface = pygame.Surface((frame_width, frame_height))
    frame_surface.blit(keyframes_image, (0, 0),
                       (left, 0, frame_width, frame_height))
    frames_list.append(frame_surface)

# 创建多个精灵对象，每个对象对应一个关键帧
all_sprites = pygame.sprite.Group()
for i in range(len(frames_list)):
    sprite = KeyframeSprite(frames_list, i)
    all_sprites.add(sprite)

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((255, 255, 255))

    # 更新和绘制所有精灵
    all_sprites.update()
    all_sprites.draw(win)

    pygame.display.flip()

pygame.quit()
