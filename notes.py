
# cd gym-2048
# pip install -e .
# cd ..

# Note: if you don't run it from 2048/, you can't import Game or Board.
# These classes need to be included in the Env, or as a separate pip package.

import gym
import gym_2048

env = gym.make('2048-v0')
observation = env.reset()

for t in range(20):
    env.render()
    # print(observation)
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
