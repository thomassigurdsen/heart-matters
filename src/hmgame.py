#! /usr/bin/python

#  hmgame.py
#
#  Copyright 2013 Thomas Sigurdsen <thomas.sigurdsen@gmail.com>
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


import pygame, sys, os
from pygame.locals import *
from player import *
from hmobject import *
from imageobject import *
from soundobject import *
from hminvisiblesprite import *
from hmglobals import DEBUG
pygame.init()

class HMGame:
	def __init__(self, screen):
		self.screen = screen
		self.background = ImageObject("Courtyard.png", (0,0))

		#pygame.transform.scale(self.srf, (1024,768))
		self.player = Player()

		# Make All interactive objects and add them to group
		self.interactive = pygame.sprite.Group()
		## ^^ Having this be a RenderUpdates type of group makes objects flicker when player is
		## standing on top of them.
		anipos = (350,400)
		wheel = hmObject("wheelbarrow.1.png","creakywheel.ogg", (150,200), (255,0,255))
		mouse = hmObject("mouse.png", "heartbeat.ogg", anipos, (255,0,255))
		mouse.visible = False
#		self.dog = hmObject ("character.png","creakywheel.ogg", (30,800), (255,0,255))
#		self.heartBeat = SoundObject("heartbeat.ogg", anipos)

#		self.interactive.add(self.heartBeat)
		self.interactive.add(wheel)
		self.interactive.add(mouse)
		self.animal = mouse

		#self.heartBeat()
		self.deltaX = 0
		self.deltaY = 0
		self.playerSpeed = 1

		## Make heart sound object
#		self.heartbeat = SoundObject("heartbeat.ogg", (345, 400))

		# Heart found bool statement
		self.heartfound = False

		## Make heart object !!!Debugging only!!
#		self.heart = ImageObject("heart.png", (145, 400), (255,0,255))

		## Make wall bounding-box.
		longwallsize = 30
		leftwallsize = 40
		rightwallsize = 120
		self.topWall = HMInvisibleSprite(0,0, self.screen.get_width(), longwallsize)
		self.bottomWall = HMInvisibleSprite(0,self.screen.get_height() - longwallsize, self.screen.get_width(), longwallsize)
		self.leftwall = HMInvisibleSprite(0,longwallsize, leftwallsize,self.screen.get_height() - (longwallsize*2))
		self.rightwall = HMInvisibleSprite(self.screen.get_width() - rightwallsize,longwallsize, rightwallsize,screen.get_width() - (longwallsize*2))
		self.wallgroup = pygame.sprite.Group((self.topWall, self.bottomWall, self.leftwall, self.rightwall))

		## Make colliding objects group, have it contain both interactive and wallgroup
		self.tree = ImageObject("tree.png", ((self.screen.get_size()[0] - 160), 100), (255,0,255))
		self.collidingObjectsGroup = pygame.sprite.RenderUpdates((self.tree, wheel, self.wallgroup))
	# __init__() end

	def update(self):
		self.eventHandler()
		# Check for collisions with collidingObjectsGroup
		for collidable in pygame.sprite.spritecollide(self.player, self.collidingObjectsGroup, False):
			if DEBUG > 1:
				print("COLLISION: COLLIDABLE")
			self.player.keyMove(-self.deltaX, -self.deltaY)
			#self.deltaX = 0
			#self.deltaY = 0
		self.displayUpdate()
		self.animal.volumeControler(self.player.rect)
	# update() end

	def eventHandler(self):
		deltaX = 0
		deltaY = 0
		if DEBUG > 3:
			print("in eventHadler")
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
					hit = False
					for interactive in pygame.sprite.spritecollide(self.player, self.interactive, False, pygame.sprite.collide_circle):
						if DEBUG > 1:
							print ("interactive hit")
						interactive.stopSound()
						hit = True
					if not hit:
						SoundObject("digging.ogg", (self.player.rect[0],self.player.rect[1]))
#					if self.player.rect.colliderect(self.heartbeat.rect):
#						self.heartfound = True
#						if DEBUG > 1:
#							print ("heart found")
#end KEYDOWN
			if event.type == KEYUP:
				if DEBUG > 1:
					print("Keyup: ", event.key)
				if event.key == K_LEFT:
					self.deltaX = 0
					#pygame.transform.rotate(self.player.image, 0):
				if event.key == K_RIGHT:
					self.deltaX = 0
					#pygame.transform.rotate(self.player.image, 180):
				if event.key == K_UP:
					self.deltaY = 0
					#pygame.transform.rotate(self.player.image, 270):
				if event.key == K_DOWN:
					self.deltaY = 0
					#pygame.transform.rotate(self.player.image, 90):
			#End KEYUP
		#End for-loop (event.pull())
		# This will be ran every update. May produce problems, but I don't think so.
		self.player.keyMove(self.deltaX, self.deltaY)
	# eventHandler() end

	def displayUpdate(self):
		if DEBUG > 2:
			print("in displayUpdate")
		#self.screen.fill(self.background)
		self.background.draw(self.screen)
		# Draw everything after drawing the background
#		if self.heartfound == True:
#			self.heart.draw(self.screen)

		pygame.display.update(self.interactive.draw(self.screen))

		self.player.draw(self.screen)
		# Flip the display after drawing, so stuff shows up on screen
		pygame.display.flip()
	# displayUpdate() end
