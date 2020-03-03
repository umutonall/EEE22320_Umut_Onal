#Umut Önal 21600216



#SORU 1
kenarA = int(input("1. Kenarı girin: "))
kenarB = int(input("2.kenarı girin: "))
print("Hesaplanıyor...")
for i in range(2):
    if kenarA > kenarB:
        kenarA /= 2
    else:
        kenarB /= 2

print("1. Kenar: " + str(int(kenarA)))
print("2. Kenar: " + str(int(kenarB)))

#SORU 2
metin1 =" Dont try to be different . Just be good . To be good is different enough ."
metin2 =" Everyone wants , happiness . No one wants pain . But you cant have a rainbow without a little rain ."
metin3 =" Consult not your fears but your hopes and your dreams . Think not about your frustrations , but about your unfulfilled potential . Concern yourself not with what you tried and failed in , but with what it is still possible for you to do."


def KelimeSayısınıHesapla(mtn):
    metin = str(mtn)
    metin = metin.replace("." , "")
    metin = metin.replace(",", "")
    while metin.count("  ") > 0:
        metin = metin.replace("  ", " ")

    count = 0
    for kelime in metin.split(" "):
        if len(kelime) > 0:
            count += 1

    return count

print("metin1deki kelime sayısı: " + str(KelimeSayısınıHesapla(metin1)))
print("metin2deki kelime sayısı: " + str(KelimeSayısınıHesapla(metin2)))
print("metin3deki kelime sayısı: " + str(KelimeSayısınıHesapla(metin3)))


#SORU 4

 # Teknolojinin ne kadar hızlı bir şekilde geliştiini ve bu gelişime ne kadar büyük fayda sağladığını görebiliyoruz. Zamanla hard disklerin boyutu küçülerek kapasitesi
 #artmış ve aynı zamanda hızıda artarak çeşitlenmiştir.


#SORU 5


soyagaci = {'Oliver': ['Anna','Harry'],
            'Isabella': ['Ralph','Emily'],
            'Ralph': ['Amelia','William'],
            'Anna': ['Amelia','William'],
            'Leo': ['Amelia','William'],
            'Amelia': ['Mia','George'],
            'George': ['Catherine','Noah'],
            'John': ['Jacob','Sophia']}


def ancestors(soyagaci, person):
    atalar = []
    if person in soyagaci.keys():
        parents = soyagaci[person]
        for ata in parents:
            atalar.append(ata)
        for ata in parents:
            ancestor = ancestors(soyagaci, ata)
            for anc in ancestor:
                atalar.append(anc)

    return atalar


print(ancestors(soyagaci,'Oliver'))
print(ancestors(soyagaci,'Ralph'))


 
