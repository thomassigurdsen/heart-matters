#! /usr/bin/python

#  imageobject.py
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

import pygame
from image import *
from hmglobals import DEBUG

class ImageObject(pygame.sprite.Sprite):
	""" Object class for image-objects.
	"""
	def __init__ (self, image, pos, colorkey=None):
		if DEBUG > 2:
			print("in Object.__init__()")
			print(imagePath)

		imagePath = "res/image/"+image
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = loadimage(imagePath, colorkey)
		screen = pygame.display.get_surface()
		self.scrArea = screen.get_rect()
		self.rect = self.rect.move(pos)
	#end __ init__

	def draw(self, screen):
		screen.blit(self.image, (self.rect[0], self.rect[1]))
	#end draw
