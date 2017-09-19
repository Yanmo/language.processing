#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
def ngram(sequences, N):
    ngram_list=list()
    for v in sequences:
        index = sequences.index(v)
        if index + N <= len(sequences):
            ngram_list.append(sequences[index:index+N])
    return ngram_list

sentence1 = "paraparaparadise"
sentence2 = "paragraph"

x = set(ngram(sentence1, 2))
y = set(ngram(sentence2, 2))
unioin = x | y
intersection = x & y
difference = x - y
print(unioin)
print(intersection)
print(difference)
