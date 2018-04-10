#readability.py
#	calculates the readability based off of algorithm(s)
#	start off w FORCAST
#-Duncan Harmon

import math
from nltk.corpus import cmudict

TEXTFILE = "name.txt"
SPLITBY  = [" " , "." , "," , ";" , ":" , "!", "?" , "(" , ")" , ]

def split(filename,splitby[]):
	file = open(filename,"r")
	rtn = []
	for i in range[0,len(file)]:
		if file[i].isalpha():
			for j in range[i+1,len(file)]:
				s = file[i:j]
				if splitby.count(file[j])!=0:
					rtn.append(s)
					i = j

	return rtn



#def wordsample(split[],samplesize):

if __name__ == '__main__':
	split(textfile,)