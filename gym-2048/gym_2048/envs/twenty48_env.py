import gym
from gym import error, spaces, utils
from gym.utils import seeding

from game import Game

class Twenty48Env(gym.Env)

    metadata = {'render.modes': ['human']}

    def __init__(self, board_size=4):
        self.game = Game()

    def _step(self, action):
        if action == 0:
            self.game.down()
        elif action == 1:
            self.game.up()
        elif action == 2:
            self.game.right()
        elif action == 3:
            self.game.left()
        else:
            raise error.Error("Unsupported action: {0}".format(action))

    def _reset(self):
        self.game = Game()

    def _render(self, mode='human', close=False):
        self.game.board.show()
