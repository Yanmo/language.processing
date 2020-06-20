#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import codecs
import io
# for python 2.x
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# for python 3.x
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
str = u"パタトクカシーー"
print(str[0::2]) #  only print odd number character.
