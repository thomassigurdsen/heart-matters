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

class hmObject(pygame.sprite.Sprite):
	""" Object class for unspecified game world object handling.
	This could just inherit more or less everything from soundobject and imageobject.
	We don't do that, because of time and familiarity.
	"""
	def __init__ (self, image, sound, pos, colorkey=None):
		if DEBUG > 2:
			print("in Object.__init__()")
			print(imagePath)
			print(soundPath)

		imagePath = "res/image/"+image
		soundPath = "res/sound/"+sound
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = loadimage(imagePath, colorkey)
		self.sound = pygame.mixer.Sound(soundPath)
		screen = pygame.display.get_surface()
		self.scrArea = screen.get_rect()
		self.rect = self.rect.move(pos)
		self.playSound()
	#end __ init__

	def draw(self, screen):
		screen.blit(self.image, (self.rect[0], self.rect[1]))
	#end draw

	def playSound(self, loop = (-1)):
		self.sound.play(loop)
	#play end

	def stopSound(self):
		self.sound.stop()
	#play end

	def volumeControler(self,playerPos):
		difX = 0
		difY = 0
		volume = 0.0

		if playerPos[0] > self.rect[0]:
			difX =  playerPos[0] - self.rect[0]
		else:
			difX =  self.rect[0] - playerPos[0]

		if playerPos[1] > self.rect[1]:
			difY =  playerPos[1] - self.rect[1]
		else:
			difY =  self.rect[1] - playerPos[1]


		#difX =  playerPos[0] - self.rect[0]
		#difY =  playerPos[1] - self.rect[1]

		difpos = pygame.math.Vector2(difX,difY)


		if DEBUG > 2:
			print(difpos)

		if difpos[0] > 200 or difpos[1] > 200:
			self.sound.set_volume(0.2)
		if difpos[0] < 200 and difpos[1] < 200:
			self.sound.set_volume(0.4)
		if difpos[0] < 100 and difpos[1] < 100:
			self.sound.set_volume(0.6)
		if difpos[0] < 50 and difpos[1] < 50:
			self.sound.set_volume(1)
	#end volumControler
#end hmObject
