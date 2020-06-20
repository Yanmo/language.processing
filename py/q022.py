#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
import itertools
import json
import gzip
import re
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
# - 1行に1記事の情報がJSON形式で格納される
# - 各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
# - ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ．
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
articles = []
target_title = "イギリス"
with gzip.open("python/references/jawiki-country.json.gz", "r") as gzipfs: 
  line = gzipfs.readline()
  while line :
    articles.append(json.loads(line))
    line = gzipfs.readline()  

  for article in articles:
    if target_title in article["title"] :
      target_article_s = article["text"]

  categories = []
  for article_line in target_article_s.split("\n"): 
    if '[[Category:' in article_line:
      categories.append(article_line)

  pattern = r'\[\[Category:(.+?)\]\]'
  for category in categories:
      match = re.search(pattern, category)
      print(match.groups()[0])
