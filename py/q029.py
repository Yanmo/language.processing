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

# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
# - 1行に1記事の情報がJSON形式で格納される
# - 各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
# - ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ．
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
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

  pattern = re.compile(r'^{{基礎情報 .+\n}}$', re.MULTILINE | re.DOTALL)
  match = re.search(pattern, target_article_s)
  wiki_strong_pattern = r"'{2,5}"
  wiki_in_anchor_pattern = r"\[\[(.+?)\]\]"
  wiki_ex_anchor_pattern = r"\[(.+?)\s*(.+?)*\]"
  wiki_tepmlate_pattern = r"\{\{(.+?)\}\}"
  markup_pattern = r"<[^>]+?>([^<]+?)</[^>]+?>"
  markup_closed_pattern = r"<[^>]+?/?>"
  basic_info = {}
  if match:
    for line in match.group().split("\n") :
      if " = " in line :
        field = line.split(" = ")
        key = field[0][1::]
        value = field[1]

        # q26
        value = re.sub(wiki_strong_pattern, "", value)

        # q27
        anchors = re.finditer(wiki_in_anchor_pattern, value)
        if anchors:
          for anchor in anchors :
            rep = anchor.group()[2:-2].split("|")[-1]
            value = value.replace(anchor.group(), rep)
        
        # q28
        value = re.sub(markup_closed_pattern, "", value)

        markups = re.finditer(markup_pattern, value)
        if markups:
          for markup in markups :
            rep = markup.groups()[0]
            value = value.replace(markup.group(), rep)

        anchors = re.finditer(wiki_ex_anchor_pattern, value)
        if anchors:
          for anchor in anchors :
            rep = " ".join(anchor.group()[1:-1].split(" ")[1::])
            value = value.replace(anchor.group(), rep) 

        templates = re.finditer(wiki_tepmlate_pattern, value)
        if templates:
          for template in templates :
            rep = template.group()[2:-2].split("|")[-1]
            value = value.replace(template.group(), rep)

        basic_info[key] = value
 
  # q29
  wiki_media_prefix = "ファイル:"
  national_flag_filename = basic_info["国旗画像"]
  URL = "https://ja.wikipedia.org/w/api.php"
  PARAMS = {
      "action": "query",
      "format": "json",
      "prop": "imageinfo",
      "iiprop": "url|user",
      "titles": wiki_media_prefix + national_flag_filename
  }

  session = requests.Session()
  res = session.get(url=URL, params=PARAMS)
  res_json = res.json()
  pages = res_json["query"]["pages"]
  for k, v in pages.items():
    national_flag_images_url = v["imageinfo"][0]["url"]
  national_flag_images = requests.get(national_flag_images_url).content
  with open(national_flag_filename, "wb") as fout:
    fout.write(national_flag_images)

