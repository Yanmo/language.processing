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
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
hightemp = "references/hightemp.txt"
hightemp_q11 = "references/q011.txt"
f = codecs.open(hightemp, "r", "utf-8")
f_h_q11 = codecs.open(hightemp_q11, "w", "utf-8")
f_h_q11.write(f.read().replace("\t", " "))
f.close
f_h_q11.close
# for check unix commmand-lines.
# cat references/hightemp.txt | tr '\t' ' ' > references/q011_cmd.txt
