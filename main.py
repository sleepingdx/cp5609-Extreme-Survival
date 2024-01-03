import sys

from codes.MyGame import MyGame
from codes.GlobalVariables import GlobalVariables


def main():
    if len(sys.argv) > 1:
        GlobalVariables.get_instance().m_role_id = int(sys.argv[1])

    """The entrance of the game"""
    game = MyGame()
    game.start()
    game.run()
    game.end()


# start game
main()
