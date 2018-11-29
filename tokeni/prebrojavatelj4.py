# -*- coding: utf-8 -*-
with open('uslovi.txt', 'w+', encoding = 'utf-8') as lista:
    recnik=dict()
    for red in lista.readlines():
        x=red.split("/t")
        prefiks=x[0]
        frekvenca=int(x[1])
        if prefiks not in recnik:
            recnik[prefiks] = frekvenca
        else:
            recnik[prefiks]+=frekvenca

