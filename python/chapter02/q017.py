#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
import itertools
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．．
hightemp = codecs.open("references/hightemp.txt", "r", "utf-8")
lines = hightemp.readlines()
union = list()
for line in lines:
    union.append(line.split()[0])
print(list(set(union)))

# check for commmand-lines
# sort -k 1,1 references/hightemp.txt | awk '{print $1}' | uniq -c
