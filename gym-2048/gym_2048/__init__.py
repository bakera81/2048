from gym.envs.registration import register

register(id='2048-v0',
         entry_point='gym_2048.envs:Twenty48Env',
)

register(id='2048-small-v0',
         entry_point='gym_2048.envs:Twenty48SmallEnv',
)
