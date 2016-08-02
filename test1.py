# -*- coding: utf-8 -*-

import sys

progress=0
for i in range(0,1000000):
	sys.stdout.write(str(progress%1))
	progress+=1
	sys.stdout.write("\r")
