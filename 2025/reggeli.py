vendegek = int(input("Vendégek száma: "))
raktar = int(input("Raktáron lévő tojások száma: "))
szukseges_tojas = round(vendegek * 3 + (vendegek * 3 * 0.1))
print(f"Ennyi vendéghez {szukseges_tojas} tojásra van szükség.")
tojas_kulonbseg = szukseges_tojas - raktar
if tojas_kulonbseg <= 0:
    print("Nem kell több tojást vásárolni.")
else:
    print(f" Kell még {tojas_kulonbseg} tojást vásárolni.")