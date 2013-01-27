#!/usr/bin/env python

#
#  image.py
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
