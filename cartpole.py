import random
import gym


def to_step(gen, observation):
    sum = 0
    for x in range(0, 4):

        sum += observation[x] * gen[x]
    if sum > 0:
        return 1
    return 0


env = gym.make('CartPole-v0').env
# env.tags['wrapper_config.TimeLimit.max_episode_steps'] = 500
gens = []
gens_size = 10
for x in range(0, gens_size):
    gens.append([random.uniform(-10000, 10000), random.uniform(-10000, 10000), random.uniform(-10000, 10000),
                 random.uniform(-10000, 10000), 0])
for ii in range(0, 100):
    print("fadfa")
    print(gens)
    gens = sorted(gens, key=lambda gen: -gen[4])
    gens2 = gens[0:(int)(len(gens) / 2)]
    gens = gens2
    for p in range(0, len(gens)):
        print(gens[p][4])
        pass
    for ran in range(0, gens_size - len(gens)):
        fir = random.randint(0, (int)((len(gens) - 1) / (1 + (int)(len(gens) / random.randint(1, 10)))))
        sec = random.randint(0, (int)((len(gens) - 1) / (1 + (int)(len(gens) / random.randint(1, 10)))))
        new_gen = []
        mutate_chance = random.uniform(0,1)
        for _ in range(0,4):
            pre1 = random.uniform(1,100)*(gens[fir][4]+1)
            pre2 = random.uniform(1,1000)*(gens[sec][4]+1)
            pre3 = random.uniform(1,1000)
            to_app = gens[fir][_]*pre1 + gens[sec][_]*pre2
            if mutate_chance < .3:
                to_app = random.uniform(-1000,1000)*pre3
                to_app /= (pre3)
            else:
                to_app /= (pre1+pre2)
            new_gen.append(to_app)
        new_gen.append(0)
        gens.append(new_gen)
        pass
    for p in range(0, len(gens)):
        gens[p][4] = 0
        pass

    for i in range(0, len(gens)):
        observation = env.reset()
        done = False
        while (True):
            gens[i][4] += 1
            if done == True:
                print(gens[i][4])
                print("FUCK")

                break
            env.render()
            observation, reward, done, info = env.step(to_step(gens[i], observation))
    pass