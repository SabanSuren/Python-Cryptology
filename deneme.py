# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 10:05:51 2020

@author: Şaban
"""
from math import pow
# Değişkenlerin tanımlanması
s = 0
i = 0
basamak = 0

# Sayının girilmesi
def sifregir(password):
    int(input("Şifre Giriniz"))
    if sifre >= 1 and sifre <= 26:
        return sifre
    else:
        def sifreleme(sifre):
            alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']
            buyukAlfabe = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
                   'W' , 'X', 'Y', 'Z'] 
            Password = ""  
     
            for i in sifre:
                if i.isupper():
                    Password += buyukAlfabe[(buyukAlfabe.index(i) + sifre) % len(alfabe)]
                else:
                    Password =  Password + alfabe[(alfabe.index(i)+sifre) % len(alfabe)]
            print("Yazinin sifrelenmis hali : " + Password)  
print("yeni Şifre",sifre)            

#while (sifre > 0):
#    #  Çevirme işleminin yapılması
#    basamak = int((sifre % 2) * pow(10, i))
#    i += 1
#    sifre = sifre // 2
#    s = s + basamak
#
#sifre = sifreleme()
#sifre = sifregir()
#sifreleme(sifre)    

# Çevrilen sayının ekrana yazdırılması
#print(s)