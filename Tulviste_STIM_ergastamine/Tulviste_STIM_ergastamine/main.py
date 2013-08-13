#!/usr/bin/python
# -*- coding: utf-8 -*-

################################
# import the necessary modules #

import VisionEgg
VisionEgg.start_default_logging(); VisionEgg.watch_exceptions()
VisionEgg.config.VISIONEGG_SYNC_SWAP = 1
VisionEgg.config.VISIONEGG_MONITOR_REFRESH_HZ = 100.0
VisionEgg.config.VISIONEGG_SCREEN_W = 1024
VisionEgg.config.VISIONEGG_SCREEN_H = 768
VisionEgg.config.VISIONEGG_HIDE_MOUSE = 1
VisionEgg.config.VISIONEGG_FRAMELESS_WINDOW = 1
VisionEgg.config.VISIONEGG_FULLSCREEN = 1
from VisionEgg.Core import *
from VisionEgg.FlowControl import Presentation
from VisionEgg.Text import *
from VisionEgg.Textures import *
from VisionEgg.MoreStimuli import *
from numpy import *
from pygame import *
import math, random, time
################################

execfile('vp_input.py')
execfile('ltp.py')

## Screen Parameters
screen = get_default_screen()
screen.parameters.bgcolor = (0.8,0.8,0.8,0.8)
mid_x  = screen.size[0]/2
mid_y  = screen.size[1]/2

## Generate Trials
execfile('functions.py')
execfile('stimuli.py')
 

pygame.mixer.quit()
pygame.mixer.init()
tms = pygame.mixer.Sound("Ergast_TMS_WhitNoise_2sek.ogg")
sham = pygame.mixer.Sound("Sham1.ogg")

TMSSHAM = str(TMScnd.get())

if TMSSHAM == 'SHAM':
        music = sham
        leng = 30.0
elif TMSSHAM == 'TMS':
        music = tms
        leng = 30.0

## Instructions
start_viewp = Viewport(screen=screen, stimuli=[text1])
screen.clear()
start_viewp.draw()
swap_buffers()
start_keypress()

## The stimulation begins

TMS_viewp = Viewport(screen=screen, stimuli=[text_TMS])
screen.clear()
TMS_viewp.draw()
swap_buffers()
start_keypress()



##################################
# start the loop over all trials #
##################################

trial = 0
pygame.event.set_allowed(KEYDOWN)
points = 0



while trial != 12:      ## Siin defineerid trialite arvu
        points += 1
        text_points.parameters.text = u"Stimuleerimisi: " + str(points)
        
        if TMSSHAM == 'SHAM':
                stimulate_viewp = Viewport(screen=screen, stimuli=[text_stimulate, text_points])
                screen.clear()
                stimulate_viewp.draw()
                swap_buffers()
                channel = music.play()
                time.sleep(leng)
                
        elif TMSSHAM == 'TMS':
                stimulate_viewp = Viewport(screen=screen, stimuli=[text_stimulate, text_points])
                screen.clear()
                stimulate_viewp.draw()
                swap_buffers()
                channel = music.play()
                setBit(lpt, 0, 1)
                setBit(lpt, 0, 0)
                time.sleep(leng)
                
        trial += 1
        
screen.close()
#write_data()

