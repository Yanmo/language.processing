#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
import itertools
import json
import gzip
import re
import requests
import MeCab

# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
# その結果をneko.txt.mecabというファイルに保存せよ．
# このファイルを用いて，以下の問に対応するプログラムを実装せよ．
# なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
option = "-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/"
mecab_tagger = MeCab.Tagger()
# mecab_tagger = MeCab.Tagger(option)

fw = open("python/references/neko.txt.mecab", "w")
fr = open("python/references/neko.txt", "r")
line = fr.readline()
while line :
    if line.strip():
        fw.write(mecab_tagger.parse(line.strip()))
    line = fr.readline()
fw.close

# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ．
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
results = []
fs = open("python/references/neko.txt.mecab", "r")
sentences = "".join(fs.readlines()).split("\nEOS\n")
for sentence in sentences: 
    tokens = []
    if sentence :
        for token in sentence.split("\n"):
            dic = {}
            if token:
                parts = token.split(",")
                dic["surface"] = parts[0].split("\t")[0]
                dic["pos"] = parts[0].split("\t")[1]
                dic["pos1"] = parts[1]
                dic["base"] = parts[-3]            
            tokens.append(dic)
        results.append(tokens)

# 動詞の表層形をすべて抽出せよ．
verb_surface = []
for tokens in results:
    for dic in tokens:
        if dic["pos"] == "動詞":
            verb_surface.append(dic["surface"])
