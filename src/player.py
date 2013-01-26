#! /usr/bin/python

#  player.py
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

import pygame
from image import *


class Player:
	""" The player class, the one and only controlled character in the game.
	"""
	def __init__ (self):
		print("in Player.__init__()")
		self.sprite = loadimage("res/image/character.png")
		self.xPos = 0
		self.yPos = 0
	#end __ init__

	def draw(self, screen):
		screen.blit(self.sprite[0], (self.xPos,self.yPos))

	#end
