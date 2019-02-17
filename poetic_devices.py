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

def dict_create_one_line(line1, line2):
	consonant_list = ["b","d","f","g","h","dʒ","k","l","m","n","p","r","s",
"t","v","w","z","ʒ","tʃ","ʃ","θ","ð","ŋ","j"]
	word_dict = {}
	for word,index in zip(line1, line2):
		if word[:1].lower() == "d":
			if word[:2].lower() == "dʒ":
				word_dict.setdefault("dʒ", []).append(index)
			word_dict.setdefault("dʒ", []).append(index)
			continue
		if word[:1].lower() == "t":
			if word[:2].lower() == "tʃ":
				word_dict.setdefault("tʃ", []).append(index)
			word_dict.setdefault("t", []).append(index)
			continue
		if word[:1].lower() in consonant_list:
			word_dict.setdefault(word[:1].lower(), []).append(index)
	return word_dict



def alliteration(word_list_per_line, transcribe_list):
	dictionary_list = [ dict_create_one_line(line,line2) for line,line2 in zip(transcribe_list,word_list_per_line)]

	main_list = []
	for each_dict in dictionary_list:
		sub_list = []
		for wl in each_dict.values():
			if len(wl) >= 2:
				for word in wl:
					sub_list.append(word)
		if len(sub_list) >= 2:
			main_list.append(sub_list)

	return main_list



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
# print_poem(poem_lines)
word_list_per_line = extract_words_per_line(poem_lines)
transcribe_list = extract_transcribed_words_per_line(poem_lines)

# for line1,line2 in zip(word_list_per_line,transcribe_list):
# 	for word1,word2 in zip(line1,line2):
# 		print(word1,word2)


#GERARD ALLITERATION LIST
allit_list = alliteration(word_list_per_line,transcribe_list)
#GERARD ONOMATOPOEIA LIST
ono_list = onomatopoeia(word_list_per_line)

# print_poem(poem_lines)
# print(allit_list)
# print(ono_list)