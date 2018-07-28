

import gym


env_name = 'Copy-v0'

env = gym.make(env_name)

action_space = env.action_space
observation_space = env.observation_space
print('action_space', action_space)
print('observation_space', observation_space)


for i_episode in range(2):
    observation = env.reset()
    for t in range(100):
        # env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break