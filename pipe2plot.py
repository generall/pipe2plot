#!/usr/bin/env python -u

"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import random
import sys
import fileinput
import getopt
import re
import math

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

class PipePlotter:

	def usage(self):
		print("Usage: pipe2plot.py [options] [files (default = stdin)]");
		print("-i           NOT Ignore unparsed values;");
		print("-b int       Buffer size ( default = infinity );");
		print("-t val       <not implemented> Template for line e.g. \"x1 y1 x2 y2\" (default=\"y1 y2 y3 ...\" );");
		print("-d val       Delimeter regexp ( default = \"\s+\" );");
		print("-s val       Style of grafs according to matplotlib;");



	def plot(self, x = None, y = None):
		if x == None:
			x = self.x;
		if y == None:
			y = self.y;
		#print("x: ", x)
		#print("y: ", y)
		self.plt.draw()
		self.plt.plot(x, y, self.style)

	'''
	detouch plot window from input
	'''
	def hold(self):
		self.plt.ioff();
		self.plt.show()

	'''
	Parse line of data input and add to storage
	'''
	def parse_line(self, line, x = None, y = None, i = None):
		# rewrite with regexp\template
		if x == None:
			x = self.x;
		if y == None:
			y = self.y;
		if i == None:
			i = self.i

		if not self.ignore_trash:
			data = re.splir(self.delim, line)
		else:
			data = filter(lambda x: isfloat(x) , re.split(self.delim, line))
		
		try:
			data = map(lambda x: float(x) ,  data)
		except:
			sys.exit(2)

		if len(self.x) > self.buff_size: # if buffer overflow, delete oldest data
			x = self.x[1:]
			y = self.y[1:]
		if self.use_pattern:
			pass
		else:
			if len(data) > 0:
				x.append([i]*len(data))
				y.append(data)
		i += 1;


	'''
	Read data from file and add to storage
	'''
	def add_from_files(self, files):
		x = []
		y = []
		size = len(files)
		colomns = int(math.sqrt(size));
		rows = math.ceil(size / float(colomns));
		n = 0;
		for fname in files:
			n += 1;
			x.append([])
			y.append([])
			self.plt.subplot(rows, colomns, n)
			self.plt.ylabel(fname)
			i = 0
			f = open(fname, "r")
			for line in f:
				self.parse_line(line,x[-1],y[-1],i);
				i += 1;
			self.plot(x[-1],y[-1])
		self.hold();

	'''
	Read unbuffered data from stdin and plot it line by line
	'''
	def read_stdin(self):
		i = 0;
		while 1:
			i += 1
			line = sys.stdin.readline()
			if line == "":
				break
			self.parse_line(line, self.x, self.y, i)
			self.plot()
		self.hold()



	def start(self, args):
		try:
			opts, files = getopt.getopt(args, "ihb:t:d:s:", ["help"])
		except getopt.GetoptError as err:
			print(str(err))
			self.usage()
			sys.exit(2)
		try:
			for o, a in opts:
				if o == "-i":
					self.ignore_trash = False;
				elif o == "-b":
					self.buff_size = int(a);
				elif o == "-t":
					self.use_pattern = True;
					self.pattern     = a;
				elif o == "-d":
					self.delim = a;
				elif o == "-s":
					self.style = a;
				elif o in ["-h", "--help"]:
					self.usage();
					sys.exit();
				else:
					assert False, "unhandled option"
		except Exception as inst:
			print(inst) 
			self.usage();
			sys.exit(2);
		#print(self.ignore_trash, self.buff_size, self.use_pattern, self.pattern, self.delim, self.files);
		#sys.exit()
		self.plt.ion()
		self.plt.show()
		if len(files) > 0:
			self.add_from_files(files);
		else:
			self.read_stdin();


	def __init__(self):
		import matplotlib.pyplot as plot
		self.plt = plot
		self.x = []
		self.y = []
		self.i = 0
		self.use_pattern = False;
		self.pattern = ""
		self.delim = "\s+"
		self.buff_size = float('inf')
		self.ignore_trash = True;
		self.style = ""


if __name__ == "__main__":
	plotter = PipePlotter();
	plotter.start(sys.argv[1:])