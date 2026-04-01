
konyvek = []
with open('adatok/konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev_ = adatok[0]
        szulev_ = int(adatok[1])
        if adatok[2]
        halev_ = int(adatok[2])
        nemzetiseg_ = adatok[3]
        cim_ = adatok[4]
        helyezes_ = int(adatok[5])
        konyv = {'nev': nev_, 'szulev': szulev_, 'halev': halev_, 'nemzetiseg': nemzetiseg_, 'cim': cim_, 'helyezes': helyezes_}
        konyvek.append(konyv)

print(f'{konyvek=}')
