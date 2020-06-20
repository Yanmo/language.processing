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
hightemp = codecs.open("python/references/hightemp.txt", "r", "utf-8").read().splitlines()
lines = list()
for line in hightemp:
    lines.append(line.split('\t'))
for line in sorted(lines, key=lambda line: line[2], reverse=True):
    print('\t'.join(line))

# check for commmand-lines
# sort -k 3r references/hightemp.txt 