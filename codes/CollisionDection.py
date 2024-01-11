from codes.Vector import Vector


class CollisionDetection:

    @staticmethod
    def detect_block_collision(collider_1, collider_2):
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
    def detect_circle_collision(collider_1, collider_2):
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
