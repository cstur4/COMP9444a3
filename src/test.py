# test.py
# Callum Howard, 2017

import gym

env = gym.make('CartPole-v0')
observation = env.reset()
total_reward = 0

for _ in range(1000):
    env.render()
    # take a random action
    observation, reward, done, info = env.step(env.action_space.sample())

    total_reward += reward

    if done:
        print("done")
        print(observation)
        print(total_reward)
        break

    # [position, velocity, angle, rotation]
    print(observation)

print(env.action_space)
print(env.observation_space)

