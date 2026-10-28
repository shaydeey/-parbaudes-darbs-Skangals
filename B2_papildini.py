# ----------------------------------------------------------------------
# B2. Funkcija ar noklusējuma likmi
# ----------------------------------------------------------------------

# Funkcijai jāatgriež cena kopā ar PVN. Noklusējuma likme ir 21. Aizpildi vietu, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Virs funkcijas pievieno komentāru # PVN 21%.

def ar_pvn(cena, likme=21):
    return cena * (1 + likme / 100)

print(ar_pvn(100))
print(ar_pvn(100, 12))
