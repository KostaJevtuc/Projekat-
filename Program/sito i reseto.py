# -*- coding: utf-8 -*-
with open("3dobro.txt", "r", encoding="utf-8") as izlaz:
    with open("3loše.txt", "r", encoding="utf-8") as pogresan:
        with open("3lošerly.txt", "w", encoding="utf-8") as rlypogresan:
            listavaljanih = [line[:-1] for line in izlaz.readlines()]
            listanevaljanih = [line[:-1] for line in pogresan.readlines()]
            for x in listanevaljanih:
                if x in listavaljanih:
                    pass
                else:
                    rlypogresan.write(x)