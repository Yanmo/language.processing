#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
def ngram(sequences, N):
    ngram_list=list()
    for v in sequences:
        index = sequences.index(v)
        if index + N <= len(sequences):
            ngram_list.append(sequences[index:index+N])
    return ngram_list

sentence = u"I am an NLPer"
words = sentence.replace(",", "").replace(".", "").split()
charcters = list("".join(sentence.replace(",", "").replace(".", "").split()))
print("-sentence is " + sentence)
print("--word bi-gram" )
print(ngram(words, 3))
print("--character bi-gram" )
print(ngram(charcters, 3))
