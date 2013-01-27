#! /usr/bin/python

#  heart-matters.py
#
#  Copyright 2013 Thomas Sigurdsen <thomas.sigurdsen@gmail.com>
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

import sys, pygame, os
sys.path.append('./src/')
from hmgame import *
pygame.init()

def main():
	""" Main function, called at start :P
	"""
	print("Welcome to Heart Matters!")
	width = 1024
	height = 768
	size = width, height

	# The screen is a pygame surface object.
	screen = pygame.display.set_mode(size, pygame.RESIZABLE)
	pygame.display.set_caption('Heart Matters')
	titleScreen(screen) # <- starts Title screen
	hmgame = HMGame(screen) # <- init game

	#for background music: ->
	#backgroundSound = pygame.mixer.Sound("res/sound/Spooky Theme.ogg")
	#backgroundSound.play(-1)

	while 1:
		hmgame.update()

# Main end


# This calls the 'main' function when this script is excecuted:
if __name__ == '__main__':
	main()
