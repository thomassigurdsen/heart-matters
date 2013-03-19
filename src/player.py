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
from spritesheet import *
from hmglobals import DEBUG

class Player(pygame.sprite.Sprite):
	""" The player class, the one and only controlled character in the game.
	"""
	def __init__ (self):
		if DEBUG > 2:
			print("in Player.__init__()")
		self.startxpos = 200
		self.startypos = 200
		pygame.sprite.Sprite.__init__(self)
#		self.image, self.rect = loadimage("res/image/playerAnimation.png", (255,0,255))
#		self.ss = spritesheet("playerAnimation.png")
#		self.image = self.ss.image_at((0,0,40,40))
		screen = pygame.display.get_surface()
		self.scrArea = screen.get_rect()

		## Sprite Animation!
		self.FPS = 120
		frames = self.FPS/12
		self.strips = [
			SpriteStripAnim('playerAnimation.png', (self.startxpos, self.startypos,40,40), 2, 1, True, frames),
			#SpriteStripAnim('Explode2.bmp', (0,0,12,12), 7, 1, True, frames),
			#SpriteStripAnim('Explode3.bmp', (0,0,48,48), 4, 1, True, frames) + SpriteStripAnim('Explode3.bmp', (48,48,48,48), 4, 1, True, frames),
			#SpriteStripAnim('Explode4.bmp', (0,0,24,24), 6, 1, True, frames),
			#SpriteStripAnim('Explode5.bmp', (0,0,48,48), 4, 1, True, frames) + SpriteStripAnim('Explode5.bmp', (48,48,48,48), 4, 1, True, frames),
		]
		self.spritenum = 0
		self.clock = pygame.time.Clock()
		self.strips[self.spritenum].iter()
		self.image = self.strips[self.spritenum].next()

		self.rect = self.image.get_rect().move(self.startxpos, self.startypos)
	#end __ init__

	def draw(self, screen):
		#screen.blit(self.image, (self.rect[0], self.rect[1]))
		screen.blit(self.image, (self.rect[0], self.rect[1]))
	#end draw

	def mouseMove(self, pos):
		if DEBUG > 2:
			print(pos)
		print("Mousemovement should not be used!")
		newpos = self.rect.move((pos[0] - self.rect[0]), (pos[1] - self.rect[1]))
		self.rect = newpos
	# end mouseMove

	def keyMove(self, deltaX, deltaY):
		if DEBUG > 2:
			print("in player.keymove")
		if DEBUG > 2:
			print("dx, dy: ", deltaX, deltaY)

		self.spritenum += 1
		if self.spritenum >= len(self.strips):
			self.spritenum = 0
		self.strips[self.spritenum].iter()

		newpos = self.rect.move((deltaX), (deltaY))
		self.rect = newpos
	# end keyMove

	def resetPosition(self):
		self.rect[0], self.rect[1] = self.startxpos, self.startypos
	#end resetPosition
