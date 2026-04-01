import random as rn
def kozte(szam1, szam2, szam3):
    if szam1 in range(szam2, szam3):
        return True
    else:
        return False

jo = []
for i in range(150):
    dobott_szam = rn.randint(1,12)
    if kozte(dobott_szam, 4, 9) == True:
        jo.append(dobott_szam)
print(f"A 150 dobásból {len(jo)} esett 4 és 8 közé.")
print(f"Ez az összes dobás {round(len(jo) / 150 * 100, 2)} százaléka")