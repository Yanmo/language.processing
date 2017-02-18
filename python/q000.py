#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
import sys
import codecs
str = "stressed"
print(str[::-1]) #why?

str2 =list(sum(zip(str),())) #string->tuple->list
str2.reverse() #reverse
print("".join(str2)) #join list->string
