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
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
args = sys.argv
if len(args) > 1:
    hightemp = codecs.open("references/hightemp.txt", "r", "utf-8")
    split_n = int(args[1])
    lines = hightemp.readlines()
    split_lines = list(itertools.zip_longest(*[iter(lines)]*split_n))
    for split_line in split_lines:
        for line in split_line:
            if line:
                print(line.replace('\n', ''))
        print('------')
# check for commmand-lines
# split -l 5 references/hightemp.txt q016.split.
