#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
import itertools
from collections import Counter
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ
hightemp = codecs.open("references/hightemp.txt", "r", "utf-8")
lines = hightemp.readlines()
one = list()
for line in lines:
    one.append(line.split()[0])

for k,v in sorted(Counter(one).items(), key=lambda value:value[1], reverse=True):
    print(str(v)+" "+k)

# check for commmand-lines
# cut -f1 references/hightemp.txt | sort | uniq -c | sort -k1 -r
