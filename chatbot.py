# Authors: Nomaan Khan and Faraz Khalid
# Steve Jobs Chatbot
# CS 4301

# Please read the readMe.txt before running this program and if you have any trouble running
# this program feel free to email me at nak150230@utdallas.edu

# This is a Steve Jobs chatbot. It extracts topic, subject and root from the user's input and 
# and uses that to find the most pertinent information from the database.

# If it cannot find a suitable reply it asks you for the most suitable reply and stores it
# in learnedData.txt and after that it can answer the same question.

# It also stores the user's name and any new information that the user provides.

# The chatbot may take upto 3 minutes to start depending on your system, so be patient!

# Have chatbot.py, database.txt, and learnedData.txt in the same folder.
# You need to run StanfordCoreNLP Server locally for this chatbot to function.

import spacy
import sys

import warnings
warnings.filterwarnings("ignore")

from stanfordcorenlp import StanfordCoreNLP
import logging
import json
import re
import nltk
import random
from os import system

# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000

class StanfordNLP:
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    @staticmethod
    def tokens_to_dict(_tokens):
        tokens = defaultdict(dict)
        for token in _tokens:
            tokens[int(token['index'])] = {
                'word': token['word'],
                'lemma': token['lemma'],
                'pos': token['pos'],
                'ner': token['ner']
            }
        return tokens

GREETING_INPUTS = ("Hello", "Hi", "Greetings", "Sup", "What's up", "Hey",)
GREETING_RESPONSES = ["Hi", "Hey", "Hi there", "Hello"]

def greeting():
    return random.choice(GREETING_RESPONSES)

if __name__ == '__main__':
    sNLP = StanfordNLP()

#nlp = spacy.load('en_core_web_sm')

#for token in doc:
 #   print(token.text, token.dep_)
  #  if 'subj' in token.dep_:
   #     print(token.text)

# Replace the target string
#filedata = filedata.replace('\n ', )

# Write the file out again
# with open('text1.txt', 'w') as file:
 # file.write(filedata)

    sentences = []
    with open('database.txt', errors = 'ignore') as input_file:
        for i, line in enumerate(input_file):
            line = re.sub(r'\b\d+(?:\.\d+)?\s+', '', line)
            line = re.sub(r'[^\w\s]', ' ', line)
            line = re.sub(r'\n', '', line)
            line = re.sub(r'  ', ' ', line)
            sentences.append(line)

    learnedData = []
    learnedRoots = []
    learnedSubject = []
    learnedObject = []
    num2 = 0
    with open('learnedData.txt', errors = 'ignore') as input_file2:
        print("hello")
        for i, line in enumerate(input_file2):
            line = re.sub(r'\b\d+(?:\.\d+)?\s+', '', line)
            line = re.sub(r'[^\w\s]', ' ', line)
            line = re.sub(r'\n', '', line)
            line = re.sub(r'  ', ' ', line)
            line2 = line.split()
            if len(line2) != 0:
                learnedRoots.append(line2[0])
                learnedSubject.append(line2[1])
                learnedObject.append(line2[2])
                sz = 3
                learnedData.append(' ')
                while sz < len(line2):
                    learnedData[num2] = learnedData[num2] + ' ' + line2[sz]
                    sz += 1
            num2 += 1


    subject_array = []
    object_array = []
    root_array = []

    nlp = spacy.load('en_core_web_sm')
    system("cls")
    num = 0
    df = 0
    for s in sentences:
        subjAdded = False
        objAdded = False
        doc = nlp(s)
        subject_array.append(' ')
        object_array.append(' ')
        porter = nltk.PorterStemmer()
        for token in doc:
            if 'subj' in token.dep_:
                ttext = porter.stem(token.text)
                if subjAdded == False:
                    subject_array[num] = ttext
                    subjAdded = True
                else:
                    subject_array[num] += ' '
                    subject_array[num] += ttext
            
            if 'obj' in token.dep_:
                otext = porter.stem(token.text)
                if objAdded == False:
                    object_array[num] = otext
                    objAdded = True
                else:
                    object_array[num] += ' '
                    object_array[num] += otext
        
        # Storing Roots
        result = sNLP.dependency_parse(s)
        root = s.split()
        index = int(result[0][2]) - 1
        stn_root = root[index]
        rtext = porter.stem(stn_root)
        root_array.append(rtext)

        num+=1

    greet = greeting() 
    name = input(greet + " What is your name?\n")
    type(name)
    name_result = sNLP.dependency_parse(name)
    name_root = name.split()
    name_index = int(name_result[0][2]) - 1
    name_root = name_root[name_index]
    print(greet + " " + name_root  + " ")
    print("Go ahead, ask me a question about Steve Jobs.")
    print("Or Enter -1 to exit.\n >")
    tt = name

    endflag = False
    while endflag == False:
        print(" ")
        foundFlag = False
        tt = " "
        tt = input(">")
        type(tt)
        if tt == '-1':
            print("Bye, " + name_root)
            sys.exit()
        doc2 = nlp(tt)

        text2 = tt
        text2 = re.sub('\?','', text2)
        #print("Annotate:", sNLP.annotate(text))
        #print("POS:", sNLP.pos(text))
        #print("Tokens:", sNLP.word_tokenize(text))
        #print("NER:", sNLP.ner(text))
        #print("Parse:", sNLP.parse(text))
        result = sNLP.dependency_parse(text2)
        root = text2.split()
        index = int(result[0][2]) - 1
        #print(root[index])
        input_root = root[index]
        input_root = porter.stem(input_root)

        usubj = " "
        uobj = " "
        for tkn in doc2:
            if 'subj' in tkn.dep_:
                usubj = porter.stem(tkn.text)
            if 'obj' in tkn.dep_:
                uobj = porter.stem(tkn.text)

        # for stn2 in sentences:
        #     result = sNLP.dependency_parse(stn2)
        #     root = stn2.split()
        #     index = int(result[0][2]) - 1
        #     if root[index].lower() == input_root:
        #         print(stn2)
        #     stn_root = root[index]
        #     print(result[0])

        # for objs in object_array:
        #     objs = objs.split()
        #     for obj in objs:
        #         if obj == uobj:
        #             print(obj)

        x = 0
        repFlag = False
        count = 0
        for r in root_array:
            if count >= 1:
                break
            objs = object_array[x].split()
            #nlp = spacy.load('en_core_web_md')
            root_tokens = nlp(root_array[x] + ' ' + input_root)

            if r.lower() == input_root:
                print(sentences[root_array.index(r)])
                repFlag = True
                foundFlag = True
                count += 1
                break
            # elif root_tokens[0].similarity(root_tokens[1]) >= 0.8:
            #     print(sentences[x])

        count = 0
        while x < len(root_array) and count < 2 and repFlag == False:
            objs = object_array[x].split()
            #nlp = spacy.load('en_core_web_md')
            root_tokens = nlp(root_array[x] + ' ' + input_root)

            if root_array[x].lower() == input_root:
                print(sentences[x])
                repFlag = True
                foundFlag = True
                count += 1
                break
            # elif root_tokens[0].similarity(root_tokens[1]) >= 0.8:
            #     print(sentences[x])
            x += 1

        x = 0
        while x < len(root_array) and repFlag != True and count < 2 and repFlag == False:
            if repFlag == False: 
                for obj in objs:
                    obj_tokens = nlp(obj + ' ' + uobj)
                    if obj == uobj:
                        print(sentences[x])
                        foundFlag = True
                        count += 1
                    # elif obj_tokens[0].similarity(obj_tokens[1]) >= 0.8:
                    #     print(sentences[x])

                    subjs = subject_array[x].split()
                    for sbj in subjs:
                        sbj_tokens = nlp(sbj + ' ' + usubj)
                        if sbj == usubj:
                            print(sentences[x])
                            foundFlag = True
                            count += 1
                            break
                        # elif sbj_tokens[0].similarity(sbj_tokens[1]) >= 0.8:
                        #     print(sentences[x])
            x += 1

        # Storing new and user data.
        if foundFlag == False:
            rsoFound = False
            rInd = -1
            sInd = -2
            oInd = -3
            for lr in learnedRoots:
                if lr == input_root:
                    rInd = learnedRoots.index(lr)
            for ls in learnedSubject:
                if ls == usubj:
                    sInd = learnedSubject.index(ls)
            for lo in learnedObject:
                if lo == uobj:
                    oInd = learnedObject.index(lo)
            if rInd == sInd or rInd == oInd:
                print(learnedData[rInd])
                rsoFound = True
            if sInd == oInd:
                print(learnedData[sInd])
                rsoFound = True

            if rsoFound == False:
                newData = input("Hmm, I don't Know.\nWhat do you think is the right answer?\n")
                type(newData)
                print("Duly noted.\nThank you!")
                learnedData.append(newData)
                learnedRoots.append(input_root)
                if usubj == " ":
                    usubj = 'usubj'
                if uobj == " ":
                    uobj = 'uobj'
                learnedSubject.append(usubj)
                learnedObject.append(uobj)
                output_file = open("learnedData.txt", "a+")
                output_file.write(input_root + ' ' + usubj  + ' ' + uobj + ' ' + newData + '\n')
                output_file.close()
