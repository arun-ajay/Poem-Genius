#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def extract_words_per_line(poem_lines):
	return [line.split() for line in poem_lines]


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
		transcribed_line = [ipa_word.string for ipa_word in result]
		transcribed_lines.append(transcribed_line)
	return transcribed_lines


def alliteration():
	print("hi")


def onomatopoeia(word, onoList):
	if (isOnomatopoeia(word)):
		onoList.append(word)
	return onoList


def isOnomatopoeia(word):
	onoFile = getfile("onomatopeia_words.txt")
	return word in onoFile


def getfile(poem_txt):
	return [line.rstrip('\n') for line in open(poem_txt)]


def print_poem(poem_lines):
	for line in poem_lines:
		print(line)


# file = input("Give me a file name: ")
poem_lines = getfile("poem.txt")
print_poem(poem_lines)
word_list_per_line = extract_words_per_line(poem_lines)
transcribe_list = extract_transcribed_words_per_line(poem_lines)

for word1,word2 in zip(word_list_per_line[0],transcribe_list[0]):
	print(word1,word2)

consonant_list = ["b","d","f","g","h","dʒ","k","l","m","n","p","r","s",
"t","v","w","z","ʒ","tʃ","ʃ","θ","ð","ŋ","j"]
print(len(consonant_list))