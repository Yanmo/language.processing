#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
txt_file_path = "references/hightemp.txt"
f = codecs.open(txt_file_path, "r", "utf-8")
lines = f.read()
print(len(lines.splitlines()))
f.close
# check unix command '$wc references/hightemp.txt'
