# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:26:47 2020

@author: Şaban
"""

def sifrele(metin):
    sifre = ""
    for k in metin:
        print(k, "=>", chr(ord(k) + 5))
        sifre = sifre + chr(ord(k) + 5)
    print(metin, " = >", sifre)
def sifrecoz(sifre): 
    metin = "" 
    for k in sifre:
        print(k, "=>", chr(ord(k) - 5))
        metin = metin + chr(ord(k) - 5)
    print(sifre, " = >", metin)