
def yazigir():
    yazi = input("Yazinizi giriniz : ")
    return yazi
def sayigir():
    sayi = int(input("Kac sayi atlatmak istiyorsunuz : "))
    if sayi >= 1 and sayi <= 26:
         return sayi

    else:
         print("Lutfen 0 ile 26 arasi bir deger giriniz")
         return sayigir()
def sifreleme(yazi):
    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']
    buyukAlfabe = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
                   'W' , 'X', 'Y', 'Z']
    sifre = ""
    
    for i in yazi:
        if i.isupper():
            sifre += buyukAlfabe[(buyukAlfabe.index(i) + sayi) % len(alfabe)]

        else:
            sifre = sifre + alfabe[(alfabe.index(i)+sayi) % len(alfabe)]
    print("Yazinin sifrelenmis hali : " + sifre)
yazi = yazigir()
sayi = sayigir()
sifreleme(yazi)



