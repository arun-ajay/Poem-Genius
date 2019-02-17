#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def ipa_transcribe():
		payload = {
		'text_to_transcribe': 'matter tip box cute',
		'submit': 'Show+transcription',
		'output_dialect': 'br',
		'output_style': 'only_tr',
		'preBracket': '',
		'postBracket': '',
		'speech_support': '1'
	}
	response = requests.post('https://tophonetics.com/', data=payload)
	soup = BeautifulSoup(response.text, 'html.parser')
	result = soup.find_all(class_='transcribed_word')
	for i in result:
		print(i.string)

def alliteration():

def onomatopoeia (word, onoList):
	if (isOnomatopoeia(word)):
		onoList.append(word)
	return onoList

def isOnomatopoeia(word):
	onoFile = getfile("onomatopeia_words.txt")
	return word in onoFile



def getfile(poem_txt):
    poem_lines = [line.rstrip('\n') for line in open (poem_txt)]
    return poem_lines
def print_poem(poem_lines):
	for line in poem_lines:
		print(line)



file = input("Give me a file name: ")
poem_lines = getfile(file)
print_poem(poem_lines)






