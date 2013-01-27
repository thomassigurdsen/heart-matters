#! /usr/bin/python

#  hmgame.py
#
#  Copyright 2013 Thomas Sigurdsen <thomas.sigurdsen@gmail.com>
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
import pygame, sys, os
from pygame.locals import *
from player import *
from hmobject import *
from imageobject import *
from soundobject import *
from hmglobals import DEBUG
pygame.init()

class HMGame:
	def __init__(self, screen):
		self.screen = screen
		self.background = 0,120,100
		self.player = Player()

		self.interactive = pygame.sprite.Group()
		self.wheel = hmObject("wheelbarrow.1.png","creakywheel.ogg", (924,200), (255,0,255))
		self.dog = hmObject ("charcater.png","creakywheel.ogg", (30,800), (255,0,255))
		self.heartBeat = SoundObject("heartbeat.ogg", (400,500))

		self.interactive.add(self.heartBeat)
		self.interactive.add(self.wheel)
		self.interactive.add(self.dog)

		#self.heartBeat()
		self.deltaX = 0
		self.deltaY = 0
		self.playerSpeed = 1

		## Make heart sound object
		self.heartbeat = SoundObject("heartbeat.ogg", (145, 400))

		# Heart found bool statement
		self.heartfound = False

		## Make heart object !!!Debugging only!!
		self.heart = ImageObject("heart.png", (145, 400), (255,0,255))

		## Make wall bounding-box.
		self.gardenWallLong0 = ImageObject("gardenWallLong.png", (0, 0))
		self.gardenWallLong1 = ImageObject("gardenWallLong.png", (0, (self.screen.get_size()[1] - 10)))
		self.gardenWallShort0 = ImageObject("gardenWallShort.png", (0, 0))
		self.gardenWallShort1 = ImageObject("gardenWallShort.png", ((self.screen.get_size()[0] - 10), 0))
		self.boundingBoxGroup = pygame.sprite.RenderUpdates((self.gardenWallLong0, self.gardenWallLong1, self.gardenWallShort0, self.gardenWallShort1))

		## Make trees.
		self.tree = ImageObject("tree.png", ((self.screen.get_size()[0] - 160), 100), (255,0,255))
		self.collidingObjectsGroup = pygame.sprite.RenderUpdates((self.tree))
	# __init__() end

	def update(self):
		self.eventHandler()
		# check for collisions with boundingBoxGroup
		for wall in pygame.sprite.spritecollide(self.player, self.boundingBoxGroup, False):
			if DEBUG > 1:
				print("COLLISION: WALL")
			self.player.keyMove(-self.deltaX, -self.deltaY)
			self.deltaX = 0
			self.deltaY = 0
		# check for collisions with collidingObjectsGroup, player first:
		for collidable in pygame.sprite.spritecollide(self.player, self.collidingObjectsGroup, False):
			if DEBUG > 1:
				print("COLLISION: COLLIDABLE")
			self.player.keyMove(-self.deltaX, -self.deltaY)
			#self.deltaX = 0
			#self.deltaY = 0
		self.displayUpdate()
		self.heartBeat.volumeControler(self.player.rect.copy())
	# update() end

	def eventHandler(self):
		deltaX = 0
		deltaY = 0
		if DEBUG > 2:
			print("in eventHadler")
		#event = pygame.event.get()

		for event in pygame.event.get():

			if event.type == QUIT:
				sys.exit(0)
# Mouse input
			if event.type == MOUSEBUTTONDOWN:
				if DEBUG > 2:
					print(pygame.event.event_name(event.type))
					print(event.button, event.pos)
				# Mouse buttons are:
				# 1 = Left
				# 2 = Middle
				# 3 = Right
#				if event.button == 1:
#					self.player.mouseMove(event.pos)
# Keyboard input
			if event.type == KEYDOWN:
				if DEBUG > 2:
						print("Keydown: ", event.key)
				if event.key == K_ESCAPE:
					sys.exit(0)
				if event.key == K_ESCAPE:
					sys.exit(0)
				if event.key == K_LEFT:
					self.deltaX -= self.playerSpeed
				if event.key == K_RIGHT:
					self.deltaX += self.playerSpeed
				if event.key == K_UP:
					self.deltaY -= self.playerSpeed
				if event.key == K_DOWN:
					self.deltaY += self.playerSpeed
				if event.key == K_r:
					self.player.resetPosition()
				if event.key == K_SPACE:
					for interactive in pygame.sprite.spritecollide(self.player, self.interactive, False):
						if DEBUG > 1:
							print ("interactive hit")
						interactive.stopSound()
					if self.player.rect.colliderect(self.heartbeat.rect):
						self.heartfound = True
						print ("heart found")

			#end KEYDOWN

			if event.type == KEYUP:
				if DEBUG > 1:
					print("Keyup: ", event.key)
				if event.key == K_LEFT:
					self.deltaX = 0
				if event.key == K_RIGHT:
					self.deltaX = 0
				if event.key == K_UP:
					self.deltaY = 0
				if event.key == K_DOWN:
					self.deltaY = 0
			#End KEYUP
		#End for-loop (event.pull())
		# This will be ran every update. May produce problems, but I don't think so.
		self.player.keyMove(self.deltaX, self.deltaY)
	# eventHandler() end

	def displayUpdate(self):
		if DEBUG > 2:
			print("in displayUpdate")
		self.screen.fill(self.background)
		# Draw everything after drawing the background
		if self.heartfound == True:
			self.heart.draw(self.screen)

		self.gardenWallLong0.draw(self.screen)
		self.gardenWallLong1.draw(self.screen)
		self.gardenWallShort0.draw(self.screen)
		self.gardenWallShort1.draw(self.screen)
		self.tree.draw(self.screen)
		self.player.draw(self.screen)
		self.wheel.draw(self.screen)
		self.dog.draw(self.screen)
		# Flip the display after drawing, so stuff shows up on screen
		pygame.display.flip()
	# displayUpdate() end
