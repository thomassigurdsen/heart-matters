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
from soundobject import *
pygame.init()

def main():
	""" Main function, called at start :P
	"""
	print("Welcome to Heart Matters!")
	width = 1024
	height = 768
	size = width, height
	gameOver = False
#	clock = pygame.time.Clock()

	# The screen is a pygame surface object.
	screen = pygame.display.set_mode(size, pygame.RESIZABLE)
	pygame.display.set_caption('Heart Matters')
	sound = SoundObject("heartbeat.ogg", (0,0))
#	titleScreen(screen,"titlescreen.png", "heartbeat.ogg") # The black & white thing.
	titleScreen(screen,"thtmInfoScreen1.png")#, "heartbeat.ogg") # Instruction page.
	titleScreen(screen,"thtmInfoScreen2.png")#, "heartbeat.ogg") # Story page.
	sound.stopSound()
	sound = None
	hmgame = HMGame(screen) # <- init game

	#for background music: ->
	#backgroundSound = pygame.mixer.Sound("res/sound/Spooky Theme.ogg")
	#backgroundSound.play(-1)

	running = True
	while running:
		hmgame.update()
		if DEBUG > 2:
			print(pygame.time.get_ticks())
		if pygame.time.get_ticks() > 30000:
			hmgame = None
			sound = SoundObject("Cardiac_Arrest(Sampler).ogg", (0,0))
			titleScreen(screen,"thtmULostScreen.png")#, "Cardiac_Arrest(Sampler).ogg")
			titleScreen(screen,"thtmCredits1.png")#, "Cardiac_Arrest(Sampler).ogg")
			titleScreen(screen,"thtmCredits2.png")#, "Cardiac_Arrest(Sampler).ogg")
			sound.stopSound()
			sound = None
			running = False

# Main end


# This calls the 'main' function when this script is excecuted:
if __name__ == '__main__':
	main()
