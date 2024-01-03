import os

current_folder = os.path.dirname(os.path.abspath(__file__))

GAME_NAME = 'Extreme Survival'  # name of the game
GAME_RESOLUTION = (960, 720)  # resolution of the game (pixel)
MAP_GRID = 10  # size of a grid (width x height pixel)
PIXELS_PER_METER = 48  # the number of pixels contained in 1 meter
BACKGROUND_COLOR = (255, 255, 255)  # background color of the game
CHARACTER_RESOLUTION = (48, 48)  # the resolution of one character
BASIC_CHARACTER_MOVE_SPEED = 2.0  # Basic move speed (m/s)
MAIN_ROLE_DIRECTORY = os.path.join(current_folder, '../res/characters/Actor1.png')  # image resource of main role
GAME_FRAME_RATE = 200  # frame rate of the game
ARRIVE_TARGET_POS_RANGE = 1  # distance from the target position, entering this range is considered to have been reached
INVALID_ID = -1  # invalid id

JSON_GAME_LEVEL_FILE = os.path.join(current_folder, "../res/json/gameLevels.json")
JSON_CHARACTERS_FILE = os.path.join(current_folder, "../res/json/characters.json")
JSON_FSM_FILE = os.path.join(current_folder, "../res/json/fsm.json")


def convert_nsec_to_msec(nanosecond):
    """Convert nanoseconds to milliseconds"""
    return nanosecond // 1000000
