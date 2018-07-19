# -*- coding: utf-8 -*-
with open('srpcor lista od 1000 reci.txt','r',encoding='utf-8') as korpus:
    recnik = [red[:-1] for red in korpus.readlines()]
    lista = ['protivu', 'protiv', 'nadri', 'preda', 'nada', 'poda', 'beza', 'raza', 'polu', 'pred', 'pret', 'vele', 'samo', 'mimo', 'među', 'bez', 'bes', 'bež', 'beš', 'van', 'pod', 'pot', 'pra', 'pre', 'pro', 'pri', 'raz', 'ras', 'raž', 'raš', 'nad', 'nat', 'naj', 'nuz', 'nus', 'oda', 'iza', 'oba', 'pa', 'po', 'do', 'iz', 'is', 'iž', 'iš', 'uz', 'us', 'už', 'uš', 'na', 'ne', 'su', 'sa', 'od', 'za', 'ot', 'ob', 'o', 'u', 's', 'z']
    listasufiksa = ['ac', 'aš', 'nik', 'anin', 'ka', 'ica', 'nje', 'će', 'đe', 'stvo', 'ina', 'ba', 'ov', 'oš', 'ost', 'er', 'ić', 'njak', 'izam', 'ija', 'ika', 'telj', 'ina', 'aj', 'tura', 'ač', ]
    prefiksi=[]
    sufiksi=[]
    def prefiksator(rec):
        for prefiks in lista:
            if rec.startswith(prefiks):
                if rec[len(prefiks):] in recnik:
                    prefiksi.append(prefiks)
                    rec=rec[len(prefiks):]
                    prefiksator(rec)
                    return prefiksi
                else:
                    for sufiks in listasufiksa:
                            if rec.endswith(sufiks):
                                prefiksi.append(prefiks)
                                sufiksi.append(sufiks)
                                return prefiksi,sufiksi
                                break
                    for prefiks2 in lista:
                        if prefiks2+rec[len(prefiks):] in recnik and prefiks!=prefiks2:
                            prefiksi.append(prefiks)
                            
                            break
                        else:
                            pass
            else:
                pass
    
    for rec in recnik:
        prefiksator(rec)
        if prefiksi!=[]:
            if sufiksi==[]:
                print(rec +' : '+str(prefiksi))
                prefiksi=[]
            else:
                print(rec +' : '+str(prefiksi)+' : '+str(sufiksi))
                prefiksi=[]
                sufiksi=[]
            

    
