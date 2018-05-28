# -*- coding: utf-8 -*-
recnik=['razloziti','prekravica','kravica','loziti','usluziti','sluziti','prepisati','preziveti','ziveti','pisati']
lista_prefiksa=[]
for i in recnik: #prolazi kroz reci u recniku
    prefiks=i[0] #prvo slovo reci
    rec=i[1:] #ostatak reci
    while rec not in recnik: #ako ostatak reci nije u recniku, oduzima jedno po jedno slovo sve dok ne bude
        prefiks+=rec[:1]
        rec=rec[1:]
        if rec=='': #ako se itteruje kroz celu rec, bez da se zadovolji uslov while petlje, moze se pretpostaviti da rec nema prefiks
            print ('nema prefiks')
            break
    else: 
       print(prefiks)
       lista_prefiksa.append(prefiks)

 
prefiks_count={j:lista_prefiksa.count(j) for j in lista_prefiksa} #broji koliko puta se prefiks pojavio u uzorku
print (prefiks_count)