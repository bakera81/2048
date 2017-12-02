import gym
from gym import error, spaces, utils
from gym.utils import seeding

from game import Game
from board import GameOver

class Twenty48Env(gym.Env):

    metadata = {'render.modes': ['human']}

    def __init__(self, board_size=4):
        self.game = Game()
        self.action_space = spaces.Discrete(4)

    def _step(self, action):
        done = False
        reward = 0.0
        try:
            if action == 0:
                reward = self.game.down()
            elif action == 1:
                reward = self.game.up()
            elif action == 2:
                reward = self.game.right()
            elif action == 3:
                reward = self.game.left()
            else:
                raise error.Error("Unsupported action: {0}".format(action))
        except GameOver:
            done = True

        observation = self.game
        info = self.game.sequence[-1]

        return observation, reward, done, info


    def _reset(self):
        self.game = Game()

    def _render(self, mode='human', close=False):
        self.game.board.show()
