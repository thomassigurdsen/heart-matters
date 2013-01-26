#! /usr/bin/python

#  hmgame.py
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

import pygame, os

class HMGame:
	def __init__(self, screen):
		self.screen = screen
		#characterFile = os.path.join("res/image","character.png")
		#character = pygame.image.load(characterFile)
	# __init__() end

	def update(self):
		self.eventHandler()
		self.displayUpdate()
	# update() end

	def eventHandler(self):
		print("in eventHadler")
	# eventHandler() end

	def displayUpdate(self):
		print("in displayUpdate")
		greenColor = 0, 255, 0 
		self.screen.fill(greenColor)
		#self.screen.blit(character)
		pygame.display.flip()
	# displayUpdate() end
