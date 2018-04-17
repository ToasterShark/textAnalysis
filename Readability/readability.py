#readability.py
#    calculates the readability based off of algorithm(s)
#    start off w FORCAST
#-Duncan Harmon

import math
import re
import random
from nltk.corpus import cmudict
import time

TEXTLIST     = ["bmovscript.txt","chembook.txt","entry.txt","crusadequiz.txt","Hitler Speech.txt","HomerPoem1.txt","Trump Speech Prepresident.txt","pastafarianism.txt","readability.py","mozillamanifesto.txt"]
SPLITBY      = [" " , "." , "," , ";" , ":" , "!", "?" , "(" , ")" , ]
SAMPLE       = 150
DICT         = cmudict.dict()

def wordsample(input,samplesize):
    if len(input)<samplesize:
        print("file too short for samplesize")
        return
    else:
        n = int(random.randrange(0,len(input)-samplesize))
        return input[n:n+samplesize]

def monosylcount(input):
    count = 0
    for word in input:
        if word.lower() in DICT:
            if len(DICT[word.lower()]) == 1:
                count+=1
        else:
            count+=1
    return count

if __name__ == '__main__':
    for name in TEXTLIST:
        st = time.clock()
        file = open(name,"r")
        input = file.read()
        input = re.split("[@0123456789\-\+\_\=(,;:\.?! )\\\*/\'\"\\n]+",input)

        samp = wordsample(input,SAMPLE)
        #print(samp)
        #print("\n")
        N = monosylcount(samp)

        GL = 20 - (N/(SAMPLE/15))
        en = time.clock()
        elaplsed = en-st
        #print("|name" + "\t|GL\t|N\t|Time Taken")
        print("NAME: " + name + "\tGRADE LEVEL: "+str(GL)+"\tMONOSYLLABIC WORDS: "+str(N)+ "\tTIME ELAPSED:" + str(elaplsed) + "\n")

