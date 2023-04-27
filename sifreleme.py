# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:26:27 2020

@author: Şaban
"""

from sezar_sifreleme import sifreleme_fonk as sfr
metin = input("şifrelenecek metni giriniz")
sfr.sifrele(metin)
sifre = input("şifresi çözümlecek metni giriniz")
sfr.sifrecoz(sifre)