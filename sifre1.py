# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:26:06 2020

@author: Şaban
"""


metin = "Saban suren"
sifre = ""
for k in metin:
    print(ord(k)) 
    print(k, "=>", chr(ord(k) + 5))
    sifre = sifre + chr(ord(k) + 5)
    print(sifre)
print(metin, " = >", sifre)

sifre = "Saban suren"
metin = "" 
for k in sifre:

    print(k, "=>", chr(ord(k) - 5))
    metin = metin + chr(ord(k) - 5)
print(sifre, " = >", metin)
print(sifre, " = >", metin)