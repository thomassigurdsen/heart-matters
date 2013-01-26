#! /usr/bin/python

#  object.py
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

import pygame
from image import *
from hmglobals import DEBUG

class Object:
	""" Object class for unspecified game world object handling.
	"""
	def __init__ (self, image, sound):
		imagePath = "res/image/"+image
		soundPath = "res/sound"+sound
		
		print(imagePath)
		print(soundPath)
		if DEBUG > 2:
			print("in Object.__init__()")
		#pygame.sprite.Sprite.__init__(self)
		#self.image, self.rect = loadimage()
		#self.sound = pygame.mixer.Sound()
		#screen = pygame.display.get_surface()
		#self.scrArea = screen.get_rect()
		#self.sound.mixer.music.play(-1,0,0)
	#end __ init__

	def draw(self, screen):
		screen.blit(self.image, (self.rect[0], self.rect[1]))
	#end draw
	
	def play(self):
		self.play(-1, 0.0)
	#play end
	
	def stop(self):
		self.stop()
	#play end
