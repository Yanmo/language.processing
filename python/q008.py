#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# - 英小文字ならば(219 - 文字コード)の文字に置換
# - その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．
def encrypt(sequences):
    encrypted = list()
    for seq in sequences:
        if seq.islower():
            encrypted.append(chr(219-ord(seq)))
        else:
            encrypted.append(seq)
    return encrypted

text = list(u"AaBbCc")
print(text)
text2 = encrypt(list(text))
print(text2)
print(encrypt(list(text2)))
