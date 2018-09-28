

import gym

# env_name = 'BipedalWalker-v2'
# env_name = 'BipedalWalkerHardcore-v2'
# env_name = 'CarRacing-v0'
# env_name = 'LunarLander-v2'
env_name = 'LunarLanderContinuous-v2'


env = gym.make(env_name)

action_space = env.action_space
observation_space = env.observation_space
observation_space_high = observation_space.high
observation_space_low = observation_space.low
print('action_space', action_space)
print('observation_space', observation_space)
print('observation_space_high', observation_space_high)
print('observation_space_low', observation_space_low)


for i_episode in range(2):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break