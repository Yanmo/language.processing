#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
hightemp = codecs.open("references/hightemp.txt", "r", "utf-8")
col1 = codecs.open("references/q012_col1.txt", "w", "utf-8")
col2 = codecs.open("references/q012_col2.txt", "w", "utf-8")

for line in hightemp.readlines():
    cols = line.split()
    col1.write(cols[0] + "\n")
    col2.write(cols[1] + "\n")
hightemp.close
col1.close
col2.close
# for check unix commmand-lines.
