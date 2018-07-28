

import gym

import gym
from gym import spaces

# 所有的env
list = gym.envs.registry.all()
print(list)

# 自己定义space
space = spaces.Discrete(8) # Set with 8 elements {0, 1, 2, ..., 7}
print(space)
for i in range(10):
    print('action', space.sample())







