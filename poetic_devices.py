#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def extract_words_per_line(poem_lines):
    return [line.split() for line in poem_lines]


def extract_transcribed_words_per_line(poem_lines):
    transcribed_lines = []
    for line in poem_lines:
        payload = {
            'intext': line,
            'ipa': 0
        }
        response = requests.post('http://upodn.com/phon.php', data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.select_one('.wrapper').find('table').find_all('font')
        transcribed_line = list(result[1].strings)[0].split()
        transcribed_lines.append(transcribed_line)
    return transcribed_lines


def alliteration():
    print("hi")


def onomatopoeia(poem_lines):
	onoFile = getfile("onomatopoeia_words.txt")
	for line in poem_lines:
		ono_list = [word for word in line if word.lower() in onoFile]
	return ono_list

def getfile(poem_txt):
	#ONLY SEPARATES LINES, DOES NOT SEPARATE WORDS!
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

ono_list = onomatopoeia(word_list_per_line)

for word in ono_list:
	print(word)

consonant_list = ["b","d","f","g","h","dʒ","k","l","m","n","p","r","s",
"t","v","w","z","ʒ","tʃ","ʃ","θ","ð","ŋ","j"]
print(len(consonant_list))
