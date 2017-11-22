#!/usr/bin/python

'''
convert a seven letter word 
to a seven digit number, ie
as a telephone number.
'''

import sys

def char2num(ref):
	dict = {
		"a":2,"b":2,"c":2,
		"d":3,"e":3,"f":3,
		"g":4,"h":4,"i":4,
		"j":5,"k":5,"l":5,
		"m":6,"n":6,"o":6,
		"p":7,"q":7,"r":7,"s":7,
		"t":8,"u":8,"v":8,
		"w":9,"x":9,"y":9,"z":9
		}

	for key, val in dict.items():
		if ref in key:
			return format(val)

def getpad(achar):
	answer = ""
	for i in achar:
		try:
			answer += char2num(i)
		except:
			print "'"+ i + "' is not a letter."
			sys.exit()
	return answer

try:
	aword = sys.argv[1]
except:
	print "Use seven letters."
	sys.exit()

if (len(aword) is not 7):
	print "Not enough characters."
	sys.exit()

print getpad(list(aword.lower()))