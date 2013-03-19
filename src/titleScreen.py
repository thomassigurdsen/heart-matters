#! /usr/bin/python

#  titlescreen.py
#
#
#  Copyright 2013 Harry Nystad <harryjnystad@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
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
