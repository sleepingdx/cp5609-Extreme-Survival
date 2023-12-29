import os

current_folder = os.path.dirname(os.path.abspath(__file__))

GAME_NAME = 'Extreme Survival'  # name of the game
GAME_RESOLUTION = (960, 720)  # resolution of the game (pixel)
MAP_GRID = 10  # size of a grid (width x height pixel)
PIXELS_PER_METER = 5  # the number of pixels contained in 1 meter
BACKGROUND_COLOR = (255, 255, 255)  # background color of the game
CHARACTER_RESOLUTION = (48, 48)  # the resolution of one character
MAIN_ROLE_DIRECTORY = os.path.join(current_folder, '../res/characters/Actor1.png')  # image resource of main role
GAME_FRAME_RATE = 200  # frame rate of the game


def convert_nsec_to_msec(nanosecond):
    """Convert nanoseconds to milliseconds"""
    return nanosecond // 1000000
