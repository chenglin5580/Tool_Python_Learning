# Gym

## Official website
[official website](https://gym.openai.com/)
[Introduction](https://gym.openai.com/docs/)
[Environments](https://gym.openai.com/envs/#algorithmic)

## Introduction

Gym is a toolkit for developing and comparing reinforcement learning algorithms. It makes no assumptions about the structure of your agent, and is compatible with any numerical computation library, such as TensorFlow or Theano.


## Installization

> pip install gym

>git clone https://github.com/openai/gym
cd gym
pip install -e .

> You can later run pip install -e .[all] to perform a full installation containing all environments. This requires installing several more involved dependencies, including cmake and a recent pip version.

## Environments

 a bare minimum example of getting something running
 > import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action


## Observations
> observation, reward, done, info = env.step(action)

## Space
> import gym
env = gym.make('CartPole-v0')
print(env.action_space)
#> Discrete(2)
print(env.observation_space)
#> Box(4,)

> print(env.observation_space.high)
#> array([ 2.4       ,         inf,  0.20943951,         inf])
print(env.observation_space.low)
#> array([-2.4       ,        -inf, -0.20943951,        -inf])

> from gym import spaces
space = spaces.Discrete(8) # Set with 8 elements {0, 1, 2, ..., 7}
x = space.sample()
assert space.contains(x)
assert space.n == 8

##  Available Environments

> **Classic control** and **toy text**: complete small-scale tasks, mostly from the RL literature. They’re here to get you started.

>  **Algorithmic**: perform computations such as adding multi-digit numbers and reversing sequences. One might object that these tasks are easy for a computer. The challenge is to learn these algorithms purely from examples. These tasks have the nice property that it’s easy to vary the difficulty by varying the sequence length.

>  **Atari**: play classic Atari games. We’ve integrated the Arcade Learning Environment (which has had a big impact on reinforcement learning research) in an easy-to-install form.

>  **2D and 3D robots**: control a robot in simulation. These tasks use the MuJoCo physics engine, which was designed for fast and accurate robot simulation. Included are some environments from a recent benchmark by UC Berkeley researchers (who incidentally will be joining us this summer). MuJoCo is proprietary software, but offers free trial licenses.


## The registry
gym.envs.registry 查看所有