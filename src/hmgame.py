#! /usr/bin/python

#  hmgame.py
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
import pygame, sys, os
from pygame.locals import *
from player import *
from object import *
from hmglobals import DEBUG
pygame.init()

class HMGame:
	def __init__(self, screen):
		self.screen = screen
		self.background = 0,120,100
		self.player = Player()
		#self.testObject = Object("Mars1.png","test.ogg")
		self.playerSpeed = 5
	# __init__() end

	def update(self):
		self.eventHandler()
		self.displayUpdate()
	# update() end

	def eventHandler(self):
		if DEBUG > 2:
			print("in eventHadler")
		event = pygame.event.poll()
		if 1:
			deltaX = 0
			deltaY = 0
			if event.type == QUIT:
				sys.exit(0)
# Mouse input
			if event.type == MOUSEBUTTONDOWN:
				if DEBUG > 1:
					print(pygame.event.event_name(event.type))
					print(event.button, event.pos)
				# Mouse buttons are:
				# 1 = Left
				# 2 = Middle
				# 3 = Right
				if event.button == 1:
					self.player.mouseMove(event.pos)
# Keyboard input
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit(0)
				if DEBUG > 2:
						print("Keydown: ", event.key)
				if event.key == K_LEFT:
					deltaX -= self.playerSpeed
				if event.key == K_RIGHT:
					deltaX += self.playerSpeed
				if event.key == K_UP:
					deltaY -= self.playerSpeed
				if event.key == K_DOWN:
					deltaY += self.playerSpeed
				if event.key == K_r:
					self.player.resetPosition()
			if event.type == KEYUP:
				if DEBUG > 2:
					print("Keyup: ", event.key)
				if event.key == K_LEFT:
					deltaX = 0
				if event.key == K_RIGHT:
					deltaX = 0
				if event.key == K_UP:
					deltaY = 0
				if event.key == K_DOWN:
					deltaY = 0
			# This will be ran every update. May produce problems, but I don't think so.
			
			if event:
				self.player.keyMove(deltaX, deltaY)
			deltaX = 0
			deltaY = 0
	# eventHandler() end

	def displayUpdate(self):
		if DEBUG > 2:
			print("in displayUpdate")
		self.screen.fill(self.background)
		# Draw everything after drawing the background
		self.player.draw(self.screen)
		# Flip the display after drawing, so stuff shows up on screen
		pygame.display.flip()
	# displayUpdate() end
