import os

current_folder = os.path.dirname(os.path.abspath(__file__))

GAME_NAME = 'Extreme Survival'  # name of the game
GAME_RESOLUTION = (960, 720)  # resolution of the game (pixel)
MAP_GRID = 48  # size of a grid (width x height pixel)
PIXELS_PER_METER = 48  # the number of pixels contained in 1 meter
BACKGROUND_COLOR = (0, 0, 0)  # background color of the game
TILE_RESOLUTION = (48, 48)  # the resolution of one tile of terrain
BLOCK_RESOLUTION = (48, 48)  # block layer
BLOCK_PLACEHOLDERS = [0, 1, 2]  # enum of placeholder in one block 0-available 1-static block 2-dynamic block
BASIC_CHARACTER_MOVE_SPEED = 2.5  # Basic move speed (m/s)
COLLIDER_RADIUS = 2.8  # Circular collider radius
BLOCK_COLLIDER_RECT = (48, 48)  # width and height of Block collider
MAIN_ROLE_DIRECTORY = os.path.join(current_folder, '../res/characters/Actor1.png')  # image resource of main role
GAME_FRAME_RATE = 200  # frame rate of the game
ARRIVE_TARGET_POS_RANGE = 1  # distance from the target position, entering this range is considered to have been reached
INVALID_ID = -1  # invalid id

JSON_GAME_LEVEL_FILE = os.path.join(current_folder, "../res/json/gameLevels.json")
JSON_CHARACTERS_FILE = os.path.join(current_folder, "../res/json/characters.json")
JSON_FSM_FILE = os.path.join(current_folder, "../res/json/fsm.json")
JSON_TERRAIN_FILE = os.path.join(current_folder, "../res/json/terrain.json")


def convert_nsec_to_msec(nanosecond):
    """Convert nanoseconds to milliseconds"""
    return nanosecond // 1000000
