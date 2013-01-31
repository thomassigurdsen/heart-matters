#  hminvisiblesprite.py
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
from hmglobals import DEBUG

class HMInvisibleSprite(pygame.sprite.Sprite):
	""" Class for collidable objects that are invisible.
	"""
	def __init__ (self, originx, originy, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect((originx, originy), (width, height))
	# end init

	def draw(self):
		if DEBUG > 0:
			print("HMInvisibleSprite: I am invisible, don't draw me.")
		pass
	# end draw
