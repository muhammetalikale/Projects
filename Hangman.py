import random
kelimeler = ["termodinamik","kalem","araba"]
kelime = kelimeler[random.randint(0,len(kelimeler)-1)]
print("Bu kelime ",len(kelime),"harftir.")
count = 0
liste = []
listee = []
say = 0
hak = 10
for n in range(1,len(kelime)+1):
    listee.append("-")
for n in kelime:
    liste.append(n)
tahmin = ""
while tahmin!=kelime:
    count+=1
    hak -=1
    harf = input("Harf veya Tahmin gir =\n")
    if isinstance(harf,str) == True:
        if harf == kelime:
            print("DOGRU!")
            break
    if tahmin == kelime:
        print("DOGRU !")
        break
    if harf in liste:
        d = liste.count(harf)
        if d == 1:
            x = liste.index(harf)
            print("Harfiniz = ",harf,"Bulundugu Basamak =",x+1)
            listee.pop(x)
            listee.insert(x,harf)
            print(listee)
        elif d>1:
            for z in range(0,len(listee)):
                if liste[z] == harf:
                    x = liste.index(harf,z)
                    print("Harfiniz = ",harf,"Bulundugu Basamak =",x+1)
                    listee.pop(x)
                    listee.insert(x,harf)
            print(listee)
    else:
        print("Böyle bir harf yok.")
        print(listee)
    print("Kalan Hak = ",hak)
    if count == 10:
        print("Simdiye kadarki tahminlerinizle olusan sonuc =\n",listee)
        tahmin = input("Hakkın doldu,kelimeyi tahmin et =\n")
        if tahmin == kelime:
            print("DOGRU !")
            break
        elif tahmin !=kelime:
            print("YANLIS !")
            break
