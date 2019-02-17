#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def extract_words_per_line(poem_lines):
	word_list_per_line = []
	for line in poem_lines:
		word_list_per_line.append(line.split())
	return word_list_per_line

def extract_transcribed_words_per_line(poem_lines):
	transcribed_lines = []
	for line in poem_lines:
		payload = {
			'text_to_transcribe': line,
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
		transcribed_line = []
		for ipa_word in result:
			print(transcribed_line.append(ipa_word))
		transcribed_lines.append(transcribed_line)
	return transcribed_line

def alliteration():
	print("hi")

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



#file = input("Give me a file name: ")
poem_lines = getfile("poem.txt")
print_poem(poem_lines)
word_list_per_line = extract_words_per_line(poem_lines)
transcribe_list = extract_transcribed_words_per_line(poem_lines)

for word1 in word_list_per_line[0]:
	print(word1)




