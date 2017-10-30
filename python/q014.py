#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
args = sys.argv
if len(args) > 1:
    hightemp = codecs.open("references/hightemp.txt", "r", "utf-8")
    head = int(args[1])
    lines = hightemp.readlines()
    for line in lines[0:head]:
        print(line.replace("\n", ""))
# check for commmand-lines
# head -n 25 references/hightemp.txt
