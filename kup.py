import math


def kup_felszin(r: float, m: float):
    return r**2*math.pi+r*math.pi*math.sqrt(r**2+m**2)


def kup_terfogat(r: float, m: float):
    return (r**2*math.pi*m)/3


print('Kúp felszín és térfogat számítása')
r = float(input('Adja meg a sugarat:'))
m = float(input('Adja meg a magasságot:'))
if r > 0 and m > 0:
    print('A felszín:', kup_felszin(r, m))
    print('A térfogat:', kup_terfogat(r, m))
else:
    print('Hiba: rossz adat!')
