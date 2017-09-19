#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
col1 = codecs.open("references/q012_col1.txt", "r", "utf-8")
col2 = codecs.open("references/q012_col2.txt", "r", "utf-8")
merge = codecs.open("references/q013.txt", "w", "utf-8")

col1_lines = col1.readlines()
col2_lines = col2.readlines()

for c1, c2 in zip(col1_lines, col2_lines):
    merge.write(c1.strip() + "\t" + c2.strip() + "\n")
col1.close
col2.close
merge.close
# check for commmand-lines
# paste references/q012_col1_cmd.txt references/q012_col2_cmd.txt > references/q013_cmd.txt
