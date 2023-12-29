import pygame

# 初始化Pygame
pygame.init()

# 设置窗口尺寸
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Character Sprite Example")

# 加载包含人物关键帧的图片
character_frames_image = pygame.image.load(
    'Actor1.png')  # 替换为你自己的关键帧图片

# 定义每个关键帧的宽度和高度
frame_width = 48
frame_height = 48

# 计算水平和垂直方向上的关键帧数量
num_frames_horizontal = character_frames_image.get_width() // frame_width
num_frames_vertical = character_frames_image.get_height() // frame_height

# 存储关键帧的列表
frames_list = []
for i in range(num_frames_vertical):
    for j in range(num_frames_horizontal):
        left = j * frame_width
        top = i * frame_height
        frame_surface = pygame.Surface((frame_width, frame_height))
        frame_surface.blit(character_frames_image, (0, 0),
                           (left, top, frame_width, frame_height))
        frames_list.append(frame_surface)

# 创建精灵类


class Character(pygame.sprite.Sprite):
    def __init__(self, frames):
        super().__init__()
        self.frames = frames  # 存储所有关键帧的图像
        self.index = 0  # 当前关键帧索引
        self.image = self.frames[self.index]  # 设置当前精灵的图像
        self.rect = self.image.get_rect()
        self.rect.center = (win_width // 2, win_height // 2)  # 初始位置在窗口中心

    def update(self):
        # 更新精灵的图像为下一帧
        self.index = (self.index + 1) % len(self.frames)
        self.image = self.frames[self.index]


# 创建人物精灵对象
character = Character(frames_list)

# 创建精灵组
all_sprites = pygame.sprite.Group()
all_sprites.add(character)

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
