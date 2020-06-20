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
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
hightemp = codecs.open("python/references/hightemp.txt", "r", "utf-8").read().splitlines()
prefectures = list()
appearance = {}
for line in hightemp:
    prefectures.append(line.split('\t')[0])
for prefecture in set(prefectures):
    appearance[prefecture] = prefectures.count(prefecture)
print(sorted(appearance.items(), key=lambda x:x[1], reverse=True))
# check for commmand-lines
# cut -f 1 python/references/hightemp.txt | sort | uniq -c | cut -d ' ' -f 4,5 | sort -r 