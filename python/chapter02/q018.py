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
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）
hightemp = codecs.open("references/hightemp.txt", "r", "utf-8")
lines = hightemp.readlines()
union = list()
for line in lines:
    union.append(line.split())
union=sorted(union, key=lambda line:line[2])
for line in union:
    print("\t".join(line))

# check for commmand-lines
#  sort -k 3,3 references/hightemp.txt
