#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
args = sys.argv
if len(args) > 1:
    hightemp = codecs.open("references/hightemp.txt", "r", "utf-8")
    tail = int(args[1])
    lines = hightemp.readlines()
    for line in lines[-tail::]:
        print(line.replace("\n",""))
# check for commmand-lines
# tail -n 25 references/hightemp.txt
