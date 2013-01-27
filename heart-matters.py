#! /usr/bin/python

#  heart-matters.py
#
#  Copyright 2013 Thomas Sigurdsen <thomas.sigurdsen@gmail.com>
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

import sys, pygame, os
sys.path.append('./src/')
from hmgame import *
from titleScreen import *
pygame.init()

def main():
	""" Main function, called at start :P
	"""
	print("Welcome to Heart Matters!")
	width = 1024
	height = 768
	size = width, height
	gameOver = False
	clock = pygame.time.Clock()

	# The screen is a pygame surface object.
	screen = pygame.display.set_mode(size, pygame.RESIZABLE)
	pygame.display.set_caption('Heart Matters')
	titleScreen(screen,"barrel.png", "heartbeat.ogg") # <- starts Title screen
	hmgame = HMGame(screen) # <- init game

	#for background music: ->
	#backgroundSound = pygame.mixer.Sound("res/sound/Spooky Theme.ogg")
	#backgroundSound.play(-1)

	while 1:
		hmgame.update()
		
		if clock.get_ticks > 30000:
			hmgame.QUIT()
			titleScreen(screen,"barrel.png", "Cardiac_Arrest(Sampler).ogg")
			hmgame = HMGame(screen)
		
# Main end


# This calls the 'main' function when this script is excecuted:
if __name__ == '__main__':
	main()
