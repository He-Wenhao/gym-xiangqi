#import os
#os.environ['SDL_AUDIODRIVER'] = 'pulseaudio'

#import pygame
#pygame.init()

from gym_xiangqi.envs import XiangQiEnv
env = XiangQiEnv()

import time

done = False
while not done:
    #time.sleep(1)
    #env.render()
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
env.close()