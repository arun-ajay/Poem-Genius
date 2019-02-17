#!/usr/bin/env python3

def getfile(poem_txt):
    poem_lines = [line.rstrip('\n') for line in open (poem_txt)]
    return poem_lines
def print_poem(poem_lines):
	for line in poem_lines:
		print(line)



file = input("Give me a file name: ")
poem_lines = getfile(file)
print_poem(poem_lines)




