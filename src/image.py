#!/usr/bin/env python

#
#  image.py
#
#  Copyright 2013 Thomas Sigurdsen <thomas.sigurdsen@gmail.com>
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
from pygame.locals import RLEACCEL
from hmglobals import DEBUG

def loadimage(path, colorkey=None):
	"""Path is the full relative path to the image file being used,
	colorkey is the colorkey to be used, if any."""
	try:
		image = pygame.image.load(path)
	except pygame.error as message:
		print('Cannot load image:', path)
		raise(message)
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
		if DEBUG > 1:
			print(image.get_colorkey())
	return image, image.get_rect()
