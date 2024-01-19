import os
import sys


def convert_nsec_to_msec(nanosecond):
    """Convert nanoseconds to milliseconds"""
    return nanosecond // 1000000


def get_current_path():
    """relative to the root directory"""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # 当程序被打包成exe文件时
    else:
        base_path = os.path.abspath(os.path.dirname(__file__))  # 在脚本中运行时
        base_path = os.path.abspath(os.path.join(base_path, os.pardir))  # 在脚本中运行时
    return base_path  # 获取同级目录的路径


def get_parent_path():
    return os.path.abspath(os.path.join(get_current_path(), os.pardir))


def get_current_dir(filename):
    return os.path.normpath(os.path.join(get_current_path(), filename))


def get_parent_dir(filename):
    return os.path.normpath(os.path.join(get_parent_path(), filename))


GAME_NAME = 'Extreme Survival'  # name of the game
GAME_RESOLUTION = (960, 720)  # resolution of the game (pixel)
MAP_GRID = 48  # size of a grid (width x height pixel)
PIXELS_PER_METER = 48  # the number of pixels contained in 1 meter
BACKGROUND_COLOR = (0, 0, 0)  # background color of the game
TILE_RESOLUTION = (48, 48)  # the resolution of one tile of terrain
BLOCK_RESOLUTION = (48, 48)  # block layer
BLOCK_PLACEHOLDERS = [0, 1, 2]  # enum of placeholder in one block 0-available 1-static block 2-dynamic block
BASIC_CHARACTER_MOVE_SPEED = 2.5  # Basic move speed (m/s)
BASIC_CHARACTER_PATROL_SPEED = 1.5  # Speed of patrolling
BASIC_CHARACTER_CHASE_SPEED = 2  # Speed of chasing
BASIC_CHARACTER_FLEE_SPEED = 3  # Speed of fleeing
COLLIDER_RADIUS = 2  # Circular collider radius
BLOCK_COLLIDER_RECT = (48, 48)  # width and height of Block collider
MAIN_ROLE_DIRECTORY = os.path.join(get_current_path(), 'res/characters/Actor1.png')  # image resource of main role
GAME_FRAME_RATE = 200  # frame rate of the game
ARRIVE_TARGET_POS_SCOPE = 1  # Entering this scope is considered to have been reached the target position
DECELERATION_SCOPE = 72  # Entering this scope is considered to decelerate the chasing speed
DECELERATION_RATE = 80 / 100  # Deceleration rate
INVALID_ID = -1  # invalid id
