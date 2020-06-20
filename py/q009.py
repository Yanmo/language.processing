#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
import random
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

def shuffled(sequences):
    shuffled = list()
    for seq in sequences:
        if len(seq) > 4:
            shuffle = list(seq[1:len(seq)-1])
            random.shuffle(shuffle)
            seq = seq[0:1] + "".join(shuffle) + seq[len(seq)-1:len(seq)]
        shuffled.append(seq)
    return shuffled

sentence = u"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(sentence)
sentence = " ".join(shuffled(list(sentence.split())))
print(sentence)
