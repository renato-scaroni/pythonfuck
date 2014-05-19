#!/usr/bin/env python

""" PythonFuck: simples e leve interpretador de brainfuck escrito em python """

########################################################################
# Escrito por Renato Scaroni <scaroni@linux.ime.usp.br>                #
########################################################################

########################################################################
# uso: passar um script com extensão .b como parametro na linha de     #
# comando, ou digitar seu programa em uma linha, quando solicitado     #
########################################################################


import os
import sys

class interpreter():
	ptr = 0
	array = [0]
	cmdBuffer = []
	saveCmdInBuffer = False
	errorLog = []
	outputString = ""

	def runLoopStructure(self):
		while not self.array[self.ptr] == 0:
			for c in self.cmdBuffer:
				self.runCMD(c)

	def runCMD(self, c):
		if c == '>':
			self.ptr += 1
			if self.ptr == len(self.array):
				self.array.append(0)
		if c == '<':
			if self.ptr > 0:
				self.ptr -= 1
		if c == '+':
			self.array[self.ptr] += 1
		if c == '-':
			self.array[self.ptr] -= 1
		if c == '.':
			if self.array[self.ptr] < 256 and self.array[self.ptr] > 0:
				# print chr(self.array[self.ptr]),
				self.outputString += chr(self.array[self.ptr])
			else:
				# print '?',
				self.outputString += '?'
			# print "("+str(self.array[self.ptr])+")",
		if c == ',':
			a = raw_input()
			try:
				self.array[self.ptr] = ord(a[0])
			except:
				print "Sei la o que vc quis dizer, eu vo embora!"
		if c == ']':
			self.saveCmdInBuffer = False
			self.runLoopStructure()

		if self.saveCmdInBuffer:
			self.cmdBuffer.append(c)

		if c == '[':
			self.saveCmdInBuffer = True
			self.cmdBuffer = []

	def executeFile(self, inputFilename):
		f = open(inputFilename, "rb")
		for line in f:
			for i in range(0, len(line)):
				self.runCMD(line[i])
		print self.outputString

	def executeString (self, s):
		for i in range(0, len(s)):
			self.runCMD(s[i])
		print self.outputString

	def main (self):
		if len(sys.argv) == 1:
			s = raw_input("digite um programa em uma fucking linha: ")
			self.executeString(s)
			return

		if '.b' in sys.argv[1] or '.bf' in sys.argv[1]:
			self.executeFile(sys.argv[1])
		else:
			print "extensao errada, seu burro"

if  __name__ =='__main__':
	i = interpreter()
	i.main()