import pygame
import pygame.sprite
from codes.Vector import Vector


class CollideDetection:

    @staticmethod
    def detect_mask_collide(sprite, new_pos, obstacle_mask, rect):
        if not sprite.rect:
            return False
        # 计算目标位置
        target_rect = sprite.rect.move(new_pos.x, new_pos.z)

        # 使用 mask 对象检测碰撞
        if obstacle_mask:
            if sprite.mask.overlap_area(obstacle_mask, (target_rect.x - rect.x, target_rect.y - rect.y)) > 0:
                # 如果发生重叠，可以在这里进行处理，比如改变颜色或者执行其他逻辑
                print("Pixel-perfect Collision")
                return True
        return False

    @staticmethod
    def detect_sprite_collide(sprite, new_pos, obstacles):
        if not sprite.rect:
            return False
        # 计算目标位置
        target_rect = sprite.rect.move(new_pos.x, new_pos.z)

        # 检查目标位置是否与其他精灵组中的任何精灵相交
        for obstacle_group in obstacles:
            for obstacle in obstacle_group:
                # 使用 mask 对象检测碰撞
                if pygame.mask.from_surface(sprite.image).overlap(pygame.mask.from_surface(obstacle.image), (
                        target_rect.x - obstacle.rect.x, target_rect.y - obstacle.rect.y)):
                    # 如果发生重叠，可以在这里进行处理，比如改变颜色或者执行其他逻辑
                    print(f"Pixel-perfect Collision with {obstacle}")
                    return True
        return False

    @staticmethod
    def detect_sprite_collide_by_different_group(group1, group2):
        # 检测像素级碰撞
        if pygame.sprite.groupcollide(group1, group2, False, False, pygame.sprite.collide_mask):
            print("Pixel-perfect Collision")
            return True
        return False

    @staticmethod
    def detect_sprite_collide_by_different_group_ex(group1, group2):
        # 检测像素级碰撞
        collisions = pygame.sprite.groupcollide(group1, group2, False, False, pygame.sprite.collide_mask)
        for sprite1, collided_sprites in collisions.items():
            for sprite2 in collided_sprites:
                return True, sprite1, sprite2
        return False, None, None

    @staticmethod
    def detect_block_collide(collider_1, collider_2):
        """
        Detect the collision between collider_1 and collider_2
        :param collider_1: (center_x, center_z, width, height)
        :param collider_2: (center_x, center_z, width, height)
        :return: T/F
        """
        # top-left, top-right, bottom-left, bottom-right
        rect_1 = (
            (collider_1[0] - collider_1[2] / 2.2, collider_1[1] - collider_1[3] / 2),
            (collider_1[0] + collider_1[2] / 2.2, collider_1[1] - collider_1[3] / 2),
            (collider_1[0] - collider_1[2] / 2.2, collider_1[1] + collider_1[3] / 2),
            (collider_1[0] + collider_1[2] / 2.2, collider_1[1] + collider_1[3] / 2)
        )
        border_1 = {
            'left': collider_1[0] - collider_1[2] / 2.2,
            'right': collider_1[0] + collider_1[2] / 2.2,
            'top': collider_1[1] - collider_1[3] / 2,
            'bottom': collider_1[1] + collider_1[3] / 2
        }
        rect_2 = (
            (collider_2[0] - collider_2[2] / 2.2, collider_2[1] - collider_2[3] / 2),
            (collider_2[0] + collider_2[2] / 2.2, collider_2[1] - collider_2[3] / 2),
            (collider_2[0] - collider_2[2] / 2.2, collider_2[1] + collider_2[3] / 2),
            (collider_2[0] + collider_2[2] / 2.2, collider_2[1] + collider_2[3] / 2)
        )
        border_2 = {
            'left': collider_2[0] - collider_2[2] / 2.2,
            'right': collider_2[0] + collider_2[2] / 2.2,
            'top': collider_2[1] - collider_2[3] / 2,
            'bottom': collider_2[1] + collider_2[3] / 2
        }
        # rect_1 includes rect_2
        for i in range(len(rect_2)):
            if (border_1['left'] <= rect_2[i][0] <= border_1['right']
                    and border_1['top'] <= rect_2[i][1] <= border_1['bottom']):
                return True
        # rect_2 includes rect_1
        for i in range(len(rect_1)):
            if (border_2['left'] <= rect_1[i][0] <= border_2['right']
                    and border_2['top'] <= rect_1[i][1] <= border_2['bottom']):
                return True
        return False

    @staticmethod
    def detect_circle_collide(collider_1, collider_2):
        """
        Detect the collision between collider_1 and collider_2
        :param collider_1: (center_x, center_z, radius)
        :param collider_2: (center_x, center_z, radius)
        :return: T/F
        """
        distance = (Vector(collider_1[0], collider_1[1]) - Vector(collider_2[0], collider_2[1])).calculate_magnitude2()
        if distance <= (collider_1[2] + collider_2[2]) ** 2:
            return True
        return False
