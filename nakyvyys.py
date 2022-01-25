# Globaali näkyvyys näkyy kaikkialla
etunimi = 'Erkki'
sukunimi = 'Esimerkki'

# Muuttuja funktion tai metodin sisällä
def kerro_nimi():
    etunimi = 'Eveliina'
    print('Etunimi on', etunimi, 'ja sukunimi on', sukunimi)
    def tervehdi():
        print('Terve', etunimi, sukunimi)
    tervehdi()

kerro_nimi()
print('Etunimi on', etunimi, 'ja sukunimi on', sukunimi)
