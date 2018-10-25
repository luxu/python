#!/usr/bin/env python3

'''
Esse programa e um simulador basico do comando grep do UNIX

Programa 3 do curso de Python e Django.
'''

#Importacao
import sys

FOUND = 0
NOT_FOUND = 1
ERROR = 2

def find(search, filename):
	__file = open(filename)
	for line in __file:
		if search in line:
			yield line.strip()
	__file.close()
def main(args):
	try:
		search = args[1]
		print(search)
	except IndexError:
		print(sys.stderr,("Usage: grep [OPTION]... PATTERN [FILE]..."))
		return(ERROR)
	filenames = args[2:]
	#print(filenames)
	ret = NOT_FOUND
	#iteracao
	for filename in filenames:
		try:
                        for line in find(search, filename):
				print("{}:{}".format(filename, line))
				ret = FOUND
		except IOError:
			print(sys.stderr,("grep.py: %s: %s" %(ex.filename, ex.strerror)))
			return(ERROR)
	return(ret)

args = sys.argv
# print(args)
ret = main(args)
print(ret)
# sys.exit(ret)
