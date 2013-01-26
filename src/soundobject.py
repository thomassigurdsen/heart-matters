#! /usr/bin/python

#  soundobject.py
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

class SoundObject(pygame.sprite.Sprite):
	""" Object class for sound-objects.
	"""
	def __init__ (self, sound):
		if DEBUG > 2:
			print("in Object.__init__()")
			print(soundPath)

		soundPath = "res/sound/"+sound
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(10,10) # This is the default size of a sound object on the map
		self.sound = pygame.mixer.Sound(soundPath)
		screen = pygame.display.get_surface()
		self.scrArea = screen.get_rect()
		self.rect = self.rect.move(400,300)
		self.playSound()
	#end __ init__

	def playSound(self):
		self.sound.play(-1)
	#play end

	def stopSound(self):
		self.sound.stop()
	#play end

	def volumeControler(self,playerPos):
		difX = 0
		difY = 0

		difX = playerPos[0] - self.rect[0]
		difY = playerPos[1] - self.rect[1]

		difpos = pygame.math.Vector2(difX,difY)
		#difpos = playerPos - self.rect
		#vectorLengt = difpos.length()
		#if DEBUG > 2:
			#print (difpos.length())

		if difpos.length() > 0.0:
			newVolume = difpos.normalize()
			if newVolume[0] > newVolume[1]:
				self.sound.set_volume(newVolume[0]/2)
				#print ("x: ")
				if DEBUG > 1:
					print(newVolume[0])
			else:
				self.sound.set_volume(newVolume[1]/2)
				#print ("y: ")
				if DEBUG > 1:
					print(newVolume[1])

			#self.sound.set_volume(newVolume/100)
			#print (newVolume/100)
	#end volumControler
