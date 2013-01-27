#! /usr/bin/python

#  titlescreen.py
#
#
#  Copyright 2013 Harry Nystad <harryjnystad@gmail.com>
#
#  This game and all content in this file is licensed under the 
#  Attribution-Noncommercial-Share Alike 3.0 version of the Creative Commons License.
#  For reference the license is given below and can also be found at 
#  http://creativecommons.org/licenses/by-nc-sa/3.0/
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#


import pygame, sys, os
from pygame.locals import *
from player import *
from hmobject import *
from hmglobals import DEBUG
pygame.init()


def titleScreen(screen,image ,sound):
		screen = screen
		background = 0,0,0
		playMenu = True
<<<<<<< HEAD
		#adds a object with image and sound
		titleScreen = hmObject("barrel.png","heartbeat.ogg", (0,0), (255,0,255))

=======

		
		#adds a object with image and sound 
		titleScreen = hmObject(image, sound, (0,0), (255,0,255))
		
>>>>>>> 19bee53... made titlescreen mulitipurpos and a gameover screen
		#Runs the title screen as long as the player dose not push the spacebar
		while playMenu:
			screen.fill(background)
			titleScreen.draw(screen)
			pygame.display.flip()

			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_SPACE:
						playMenu = False
						titleScreen.stopSound()
